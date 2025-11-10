# IFSC1202#!/usr/bin/env python3
"""
multi_ping.py

Usage:
    python multi_ping.py hosts.txt
    python multi_ping.py 8.8.8.8 example.com 192.168.1.1

hosts.txt should contain one host per line (IP or hostname), blank lines and lines
starting with '#' are ignored.

Output:
    Prints a simple table to stdout and writes results to ping_results.csv
"""

import asyncio
import sys
import platform
import csv
import re
from datetime import datetime
from pathlib import Path

# Configuration
CONCURRENCY = 200          # number of simultaneous pings
PING_COUNT_FLAG = "-c"     # default; will be switched for Windows
DEFAULT_TIMEOUT = 3.0      # seconds to wait for one ping
OUTPUT_CSV = "ping_results.csv"

# Helper to build ping command depending on platform
def build_ping_cmd(host: str) -> list:
    system = platform.system().lower()
    if system == "windows":
        # On Windows: ping -n 1 host  (timeout handling done by asyncio.wait_for)
        return ["ping", "-n", "1", host]
    else:
        # On Linux/macOS: ping -c 1 host
        return ["ping", "-c", "1", host]

# Try to parse round-trip time (ms) from ping output (many common formats)
def parse_rtt(output: str) -> float | None:
    # common patterns: time=12.3 ms  or time<1ms  or time=12ms
    m = re.search(r"time[=<]\s*([0-9]+(?:\.[0-9]+)?)\s*ms", output, re.IGNORECASE)
    if m:
        try:
            return float(m.group(1))
        except Exception:
            return None

    # Linux summary line: rtt min/avg/max/mdev = 10.123/10.123/10.123/0.000 ms
    m2 = re.search(r"rtt .* = ([0-9\.]+)/([0-9\.]+)/([0-9\.]+)/([0-9\.]+) ms", output)
    if m2:
        try:
            return float(m2.group(2))  # average
        except Exception:
            return None

    # On some BSD/mac: round-trip min/avg/max/stddev = 10.123/10.123/10.123/0.000 ms
    m3 = re.search(r"round-trip .* = ([0-9\.]+)/([0-9\.]+)/([0-9\.]+)/([0-9\.]+) ms", output)
    if m3:
        try:
            return float(m3.group(2))
        except Exception:
            return None

    return None

async def ping_one(host: str, sem: asyncio.Semaphore, timeout: float) -> dict:
    cmd = build_ping_cmd(host)
    async with sem:
        start = datetime.utcnow()
        try:
            proc = await asyncio.create_subprocess_exec(
                *cmd,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.STDOUT
            )
            try:
                stdout, _ = await asyncio.wait_for(proc.communicate(), timeout=timeout)
            except asyncio.TimeoutError:
                # kill process if it hasn't exited
                proc.kill()
                await proc.wait()
                return {
                    "host": host,
                    "reachable": False,
                    "rtt_ms": None,
                    "error": f"timeout after {timeout}s",
                    "timestamp": start.isoformat() + "Z",
                }

            output = stdout.decode(errors="ignore")
            # On Windows, ping returns 0 exit code when reply received, nonzero when unreachable.
            reachable = (proc.returncode == 0)
            rtt = parse_rtt(output)
            return {
                "host": host,
                "reachable": reachable,
                "rtt_ms": rtt,
                "error": None if reachable else "unreachable",
                "raw_output": output,
                "timestamp": start.isoformat() + "Z",
            }
        except FileNotFoundError:
            return {
                "host": host,
                "reachable": False,
                "rtt_ms": None,
                "error": "ping command not found on this system",
                "timestamp": start.isoformat() + "Z",
            }
        except Exception as e:
            return {
                "host": host,
                "reachable": False,
                "rtt_ms": None,
                "error": str(e),
                "timestamp": start.isoformat() + "Z",
            }

async def run_many(hosts: list[str], concurrency: int, timeout: float) -> list[dict]:
    sem = asyncio.Semaphore(concurrency)
    tasks = [asyncio.create_task(ping_one(h, sem, timeout)) for h in hosts]
    results = await asyncio.gather(*tasks)
    return results

def read_hosts_from_file(path: Path) -> list[str]:
    hosts = []
    for line in path.read_text().splitlines():
        s = line.strip()
        if not s or s.startswith("#"):
            continue
        hosts.append(s)
    return hosts

def save_csv(results: list[dict], filename: str):
    keys = ["host", "timestamp", "reachable", "rtt_ms", "error"]
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        for r in results:
            row = {k: r.get(k) for k in keys}
            writer.writerow(row)

def pretty_print(results: list[dict]):
    # simple table
    widths = {"host": 30, "status": 10, "rtt": 8, "err": 25}
    print(f"{'HOST':{widths['host']}}  {'STATUS':{widths['status']}}  {'RTT(ms)':{widths['rtt']}}  {'ERROR':{widths['err']}}")
    print("-" * (widths['host'] + widths['status'] + widths['rtt'] + widths['err'] + 8))
    for r in results:
        host = (r['host'][:widths['host']-1] + "...") if len(r['host'])>widths['host'] else r['host']
        status = "UP" if r['reachable'] else "DOWN"
        rtt = f"{r['rtt_ms']:.2f}" if isinstance(r['rtt_ms'], (int,float)) else "-"
        err = r['error'] or "-"
        print(f"{host:{widths['host']}}  {status:{widths['status']}}  {rtt:{widths['rtt']}}  {err:{widths['err']}}")

def parse_args(argv: list[str]) -> tuple[list[str], int, float]:
    # Basic positional parsing: hosts file or list of hosts. Could be extended later.
    if len(argv) < 2:
        print("Usage: python multi_ping.py hosts.txt  OR python multi_ping.py host1 host2 ...")
        sys.exit(1)
    if len(argv) == 2 and Path(argv[1]).is_file():
        hosts = read_hosts_from_file(Path(argv[1]))
    else:
        hosts = argv[1:]
    return hosts, CONCURRENCY, DEFAULT_TIMEOUT

def main():
    hosts, concurrency, timeout = parse_args(sys.argv)
    if not hosts:
        print("No hosts provided.")
        sys.exit(1)

    print(f"Pinging {len(hosts)} host(s) with concurrency={concurrency}, timeout={timeout}s ...")
    results = asyncio.run(run_many(hosts, concurrency,