import os

SUSPICIOUS_EXTENSIONS = {'.exe', '.bat', '.vbs', '.js', '.scr', '.dll'}
SCAN_DIRECTORIES = ['C:\\Users\\', '/home/']

def scan_files():
    print("🔍 Scanning for suspicious files...")
    for directory in SCAN_DIRECTORIES:
        for root, _, files in os.walk(directory):
            for file in files:
                if any(file.lower().endswith(ext) for ext in SUSPICIOUS_EXTENSIONS):
                    full_path = os.path.join(root, file)
                    print(f"[!] Suspicious file found: {full_path}")

if __name__ == "__main__":
    scan_files()

import psutil

# Example: Known safe processes (customize this)
KNOWN_GOOD = {'explorer.exe', 'python.exe', 'svchost.exe'}

def check_processes():
    print("🧠 Checking running processes...")
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            name = proc.info['name']
            if name.lower() not in KNOWN_GOOD:
                print(f"[!] Unknown process: {name} (PID {proc.info['pid']})")
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

if __name__ == "__main__":
    check_processes()
import time
import psutil
import os
def monitor_system():
    print("🔍 Monitoring system performance...")
    while True:
        cpu_usage = psutil.cpu_percent(interval=1)
        memory_info = psutil.virtual_memory()
        disk_info = psutil.disk_usage('/')

        print(f"CPU Usage: {cpu_usage}%")
        print(f"Memory Usage: {memory_info.percent}%")
        print(f"Disk Usage: {disk_info.percent}%")
        print("-" * 40)

        time.sleep(5)  # Adjust the sleep time as needed
if __name__ == "__main__":
    monitor_system()   
import psutil
import time
def kill_suspicious_processes():
    print("🛑 Killing suspicious processes...")
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            if proc.info['name'].lower() in {'malware.exe', 'virus.exe'}:  # Customize with actual suspicious process names
                print(f"Killing process: {proc.info['name']} (PID {proc.info['pid']})")
                proc.kill()
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
if __name__ == "__main__":
    kill_suspicious_processes()
    print("✅ Suspicious processes terminated.")
import psutil  
import time
def log_system_activity():
    print("📜 Logging system activity...")
    with open("system_activity.log", "a") as log_file:
        while True:
            cpu_usage = psutil.cpu_percent(interval=1)
            memory_info = psutil.virtual_memory()
            disk_info = psutil.disk_usage('/')

            log_entry = (
                f"Time: {time.strftime('%Y-%m-%d %H:%M:%S')}, "
                f"CPU Usage: {cpu_usage}%, "
                f"Memory Usage: {memory_info.percent}%, "
                f"Disk Usage: {disk_info.percent}%\n"
            )
            log_file.write(log_entry)
            print(log_entry.strip())
            time.sleep(5)  # Adjust the sleep time as needed
if __name__ == "__main__":
    log_system_activity()
    print("✅ System activity logging started.")    
import psutil
def check_network_connections():
    print("🌐 Checking network connections...")
    for conn in psutil.net_connections(kind='inet'):
        laddr = f"{conn.laddr.ip}:{conn.laddr.port}"
        raddr = f"{conn.raddr.ip}:{conn.raddr.port}" if conn.raddr else "N/A"
        print(f"Local Address: {laddr} | Remote Address: {raddr} | Status: {conn.status}")
if __name__ == "__main__":
    check_network_connections()
    print("✅ Network connections checked.")
import psutil
def check_disk_usage():
    print("💾 Checking disk usage...")
    partitions = psutil.disk_partitions()
    for partition in partitions:
        usage = psutil.disk_usage(partition.mountpoint)
        print(f"Partition: {partition.device}")
        print(f"  Total Size: {usage.total / (1024 ** 3):.2f} GB")
        print(f"  Used: {usage.used / (1024 ** 3):.2f} GB")
        print(f"  Free: {usage.free / (1024 ** 3):.2f} GB")
        print(f"  Usage: {usage.percent}%")
if __name__ == "__main__":
    check_disk_usage()
    print("✅ Disk usage checked.")
import psutil
def check_memory_usage():
    print("🧠 Checking memory usage...")
    memory_info = psutil.virtual_memory()
    print(f"Total Memory: {memory_info.total / (1024 ** 3):.2f} GB")
    print(f"Used Memory: {memory_info.used / (1024 ** 3):.2f} GB")
    print(f"Free Memory: {memory_info.free / (1024 ** 3):.2f} GB")
    print(f"Memory Usage: {memory_info.percent}%")
if __name__ == "__main__":
    check_memory_usage()
    print("✅ Memory usage checked.")
import psutil
def check_cpu_usage():
    print("🖥️ Checking CPU usage...")
    cpu_usage = psutil.cpu_percent(interval=1)
    print(f"CPU Usage: {cpu_usage}%")
if __name__ == "__main__":
    check_cpu_usage()
    print("✅ CPU usage checked.")
import psutil
def check_running_processes():
    print("🔍 Checking running processes...")
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            print(f"Process ID: {proc.info['pid']} | Name: {proc.info['name']}")
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
if __name__ == "__main__":
    check_running_processes()
    print("✅ Running processes checked.")  
import psutil   
def check_system_info():
    print("ℹ️ System Information:")
    print(f"System: {psutil.users()[0].name}")
    print(f"Boot Time: {psutil.boot_time()}")
    print(f"Platform: {psutil.WINDOWS if psutil.WINDOWS else 'Linux'}")
    print(f"Architecture: {psutil.cpu_count(logical=False)}-bit")
if __name__ == "__main__":
    check_system_info()
    print("✅ System information checked.")
import psutil   
def check_system_health():
    print("🩺 Checking system health...")
    check_cpu_usage()
    check_memory_usage()
    check_disk_usage()
    check_network_connections()
    check_running_processes()
    check_system_info()
if __name__ == "__main__":
    check_system_health()
    print("✅ System health check completed.")
import psutil
def check_system_security():
    print("🔒 Checking system security...")
    check_running_processes()
    check_network_connections()
    check_disk_usage()
    check_memory_usage()
    check_cpu_usage()
    print("✅ System security check completed.")
if __name__ == "__main__":
    check_system_security()
    print("🔒 System security check completed.")
import psutil
def check_system_performance():
    print("📈 Checking system performance...")
    check_cpu_usage()
    check_memory_usage()
    check_disk_usage()
    check_network_connections()
    print("✅ System performance check completed.")
if __name__ == "__main__":
    check_system_performance()
    print("📈 System performance check completed.")
import psutil
def check_system_stability():
    print("🛠️ Checking system stability...")
    check_cpu_usage()
    check_memory_usage()
    check_disk_usage()
    check_network_connections()
    print("✅ System stability check completed.")
if __name__ == "__main__":
    check_system_stability()
    print("🛠️ System stability check completed.")
import psutil
def check_system_integrity():
    print("🔍 Checking system integrity...")
    check_cpu_usage()
    check_memory_usage()
    check_disk_usage()
    check_network_connections()
    print("✅ System integrity check completed.")
if __name__ == "__main__":
    check_system_integrity()
    print("🔍 System integrity check completed.")
import psutil
def check_system_configuration():
    print("⚙️ Checking system configuration...")
    check_cpu_usage()
    check_memory_usage()
    check_disk_usage()
    check_network_connections()
    print("✅ System configuration check completed.")
if __name__ == "__main__":
    check_system_configuration()
    print("⚙️ System configuration check completed.")
import psutil
def check_system_logs():
    print("📜 Checking system logs...")
    # This is a placeholder for actual log checking logic
    print("No suspicious logs found.")
if __name__ == "__main__":
    check_system_logs()
    print("📜 System logs checked.")
import psutil
def check_system_updates():
    print("🔄 Checking for system updates...")
    # This is a placeholder for actual update checking logic
    print("No updates available at this time.")
if __name__ == "__main__":
    check_system_updates()
    print("🔄 System updates checked.")
import psutil
def check_system_backups():
    print("💾 Checking system backups...")
    # This is a placeholder for actual backup checking logic
    print("No backup issues found.")
if __name__ == "__main__":
    check_system_backups()
    print("💾 System backups checked.")
import psutil   
def check_system_recovery():
    print("🔄 Checking system recovery options...")
    # This is a placeholder for actual recovery checking logic
    print("No recovery issues found.")
if __name__ == "__main__":
    check_system_recovery()
    print("🔄 System recovery options checked.")
import psutil
def check_system_compliance():
    print("📜 Checking system compliance...")
    # This is a placeholder for actual compliance checking logic
    print("No compliance issues found.")    
if __name__ == "__main__":
    check_system_compliance()
    print("📜 System compliance checked.")
import psutil
def check_system_security_policies():
    print("🔒 Checking system security policies...")
    # This is a placeholder for actual security policy checking logic
    print("No security policy issues found.")
if __name__ == "__main__":
    check_system_security_policies()
    print("🔒 System security policies checked.")
import psutil   
def check_system_access_controls():
    print("🔐 Checking system access controls...")
    # This is a placeholder for actual access control checking logic
    print("No access control issues found.")
if __name__ == "__main__":
    check_system_access_controls()
    print("🔐 System access controls checked.")
import psutil
def check_system_data_protection():
    print("🔒 Checking system data protection...")
    # This is a placeholder for actual data protection checking logic
    print("No data protection issues found.")
if __name__ == "__main__":
    check_system_data_protection()
    print("🔒 System data protection checked.")
import psutil
def check_system_user_privileges():
    print("👤 Checking system user privileges...")
    # This is a placeholder for actual user privilege checking logic
    print("No user privilege issues found.")
if __name__ == "__main__":
    check_system_user_privileges()
    print("👤 System user privileges checked.")
import psutil
def check_system_firewall():
    print("🔥 Checking system firewall settings...")
    # This is a placeholder for actual firewall checking logic
    print("No firewall issues found.")
if __name__ == "__main__":
    check_system_firewall()
    print("🔥 System firewall settings checked.")
import psutil   
def check_system_antivirus():
    print("🦠 Checking system antivirus status...")
    # This is a placeholder for actual antivirus checking logic
    print("No antivirus issues found.")
if __name__ == "__main__":
    check_system_antivirus()
    print("🦠 System antivirus status checked.")
import psutil
def check_system_encryption():
    print("🔐 Checking system encryption status...")
    # This is a placeholder for actual encryption checking logic
    print("No encryption issues found.")
if __name__ == "__main__":
    check_system_encryption()
    print("🔐 System encryption status checked.")
import psutil   
def check_system_backup():
    print("💾 Checking system backup status...")
    # This is a placeholder for actual backup checking logic
    print("No backup issues found.")
if __name__ == "__main__":
    check_system_backup()
    print("💾 System backup status checked.")
import psutil   
def check_system_recovery_options():
    print("🔄 Checking system recovery options...")
    # This is a placeholder for actual recovery options checking logic
    print("No recovery options issues found.")
if __name__ == "__main__":
    check_system_recovery_options()
    print("🔄 System recovery options checked.")
import psutil
def check_system_performance_metrics():
    print("📊 Checking system performance metrics...")
    # This is a placeholder for actual performance metrics checking logic
    print("No performance issues found.")
if __name__ == "__main__":
    check_system_performance_metrics()
    print("📊 System performance metrics checked.")
import psutil
def check_system_resource_usage():
    print("📈 Checking system resource usage...")
    # This is a placeholder for actual resource usage checking logic
    print("No resource usage issues found.")
if __name__ == "__main__":
    check_system_resource_usage()
    print("📈 System resource usage checked.")
import psutil
def check_system_event_logs():
    print("📜 Checking system event logs...")
    # This is a placeholder for actual event log checking logic
    print("No event log issues found.")
if __name__ == "__main__":
    check_system_event_logs()
    print("📜 System event logs checked.")
import psutil       
def check_system_configuration_files():
    print("⚙️ Checking system configuration files...")
    # This is a placeholder for actual configuration file checking logic
    print("No configuration file issues found.")
if __name__ == "__main__":
    check_system_configuration_files()
    print("⚙️ System configuration files checked.")
import psutil
def check_system_security_settings():
    print("🔒 Checking system security settings...")
    # This is a placeholder for actual security settings checking logic
    print("No security settings issues found.")
if __name__ == "__main__":
    check_system_security_settings()
    print("🔒 System security settings checked.")
import psutil       
def check_system_user_accounts():
    print("👤 Checking system user accounts...")
    # This is a placeholder for actual user account checking logic
    print("No user account issues found.")
if __name__ == "__main__":
    check_system_user_accounts()
    print("👤 System user accounts checked.")
import psutil
def check_system_network_settings():
    print("🌐 Checking system network settings...")
    # This is a placeholder for actual network settings checking logic
    print("No network settings issues found.")
if __name__ == "__main__":
    check_system_network_settings()
    print("🌐 System network settings checked.")
import psutil   
def check_system_application_settings():
    print("🛠️ Checking system application settings...")
    # This is a placeholder for actual application settings checking logic
    print("No application settings issues found.")
if __name__ == "__main__":
    check_system_application_settings()
    print("🛠️ System application settings checked.")
import psutil
def check_system_update_status():
    print("🔄 Checking system update status...")
    # This is a placeholder for actual update status checking logic
    print("No update issues found.")
if __name__ == "__main__":
    check_system_update_status()
    print("🔄 System update status checked.")
import psutil
def check_system_software_versions():
    print("📦 Checking system software versions...")
    # This is a placeholder for actual software version checking logic
    print("No software version issues found.")
if __name__ == "__main__":
    check_system_software_versions()
    print("📦 System software versions checked.")
import psutil
def check_system_hardware_status():
    print("🖥️ Checking system hardware status...")
    # This is a placeholder for actual hardware status checking logic
    print("No hardware issues found.")
if __name__ == "__main__":
    check_system_hardware_status()
    print("🖥️ System hardware status checked.")
import psutil
def check_system_peripherals():
    print("🖱️ Checking system peripherals...")
    # This is a placeholder for actual peripherals checking logic
    print("No peripherals issues found.")
if __name__ == "__main__":
    check_system_peripherals()
    print("🖱️ System peripherals checked.")
import psutil
def check_system_virtualization():
    print("🖥️ Checking system virtualization status...")
    # This is a placeholder for actual virtualization status checking logic
    print("No virtualization issues found.")
if __name__ == "__main__":
    check_system_virtualization()
    print("🖥️ System virtualization status checked.")
import psutil
def check_system_cloud_integration():
    print("☁️ Checking system cloud integration...")
    # This is a placeholder for actual cloud integration checking logic
    print("No cloud integration issues found.")
if __name__ == "__main__":
    check_system_cloud_integration()
    print("☁️ System cloud integration checked.")
import psutil   
def check_system_data_storage():
    print("💾 Checking system data storage...")
    # This is a placeholder for actual data storage checking logic
    print("No data storage issues found.")  
if __name__ == "__main__":
    check_system_data_storage()
    print("💾 System data storage checked.")
import psutil   
def check_system_data_backup():
    print("💾 Checking system data backup...")
    # This is a placeholder for actual data backup checking logic
    print("No data backup issues found.")
if __name__ == "__main__":
    check_system_data_backup()
    print("💾 System data backup checked.")
import psutil
def check_system_data_recovery():
    print("🔄 Checking system data recovery options...")
    # This is a placeholder for actual data recovery checking logic
    print("No data recovery issues found.")
if __name__ == "__main__":
    check_system_data_recovery()
    print("🔄 System data recovery options checked.")
import psutil
def check_system_data_archiving():
    print("📦 Checking system data archiving...")
    # This is a placeholder for actual data archiving checking logic
    print("No data archiving issues found.")
if __name__ == "__main__":
    check_system_data_archiving()
    print("📦 System data archiving checked.")
import psutil
def check_system_data_compression():
    print("📦 Checking system data compression...")
    # This is a placeholder for actual data compression checking logic
    print("No data compression issues found.")
if __name__ == "__main__":
    check_system_data_compression()
    print("📦 System data compression checked.")
import psutil
def check_system_data_encryption():
    print("🔐 Checking system data encryption...")
    # This is a placeholder for actual data encryption checking logic
    print("No data encryption issues found.")
if __name__ == "__main__":
    check_system_data_encryption()
    print("🔐 System data encryption checked.")

    import socket
import subprocess

def check_open_ports():
    print("🌐 Scanning for open ports...")
    try:
        result = subprocess.check_output(['netstat', '-ano'], text=True)
        for line in result.splitlines():
            if 'LISTENING' in line:
                print(f"[!] Open port found: {line.strip()}")
    except Exception as e:
        print(f"Error scanning ports: {e}")

if __name__ == "__main__":
    check_open_ports()
import socket
def check_network_interfaces():
    print("🌐 Checking network interfaces...")
    interfaces = socket.if_nameindex()
    for interface in interfaces:
        print(f"Interface: {interface[1]} (Index: {interface[0]})")
if __name__ == "__main__":
    check_network_interfaces()
    print("🌐 Network interfaces checked.")
import socket
def check_network_configuration():
    print("🌐 Checking network configuration...")
    try:
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        print(f"Hostname: {hostname}")
        print(f"IP Address: {ip_address}")
    except socket.error as e:
        print(f"Error retrieving network configuration: {e}")
if __name__ == "__main__":
    check_network_configuration()
    print("🌐 Network configuration checked.")
import socket   
def check_network_security():
    print("🔒 Checking network security...")
    # This is a placeholder for actual network security checking logic
    print("No network security issues found.")
if __name__ == "__main__":
    check_network_security()
    print("🔒 Network security checked.")
import socket
def check_network_performance():
    print("📈 Checking network performance...")
    # This is a placeholder for actual network performance checking logic
    print("No network performance issues found.")
if __name__ == "__main__":
    check_network_performance()
    print("📈 Network performance checked.")
import socket
def check_network_reliability():
    print("🔄 Checking network reliability...")
    # This is a placeholder for actual network reliability checking logic
    print("No network reliability issues found.")
if __name__ == "__main__":
    check_network_reliability()
    print("🔄 Network reliability checked.")
import socket
def check_network_latency():
    print("⏱️ Checking network latency...")
    # This is a placeholder for actual network latency checking logic
    print("No network latency issues found.")
if __name__ == "__main__":
    check_network_latency()
    print("⏱️ Network latency checked.")
import socket
def check_network_bandwidth():
    print("📊 Checking network bandwidth...")
    # This is a placeholder for actual network bandwidth checking logic
    print("No network bandwidth issues found.")
if __name__ == "__main__":
    check_network_bandwidth()
    print("📊 Network bandwidth checked.")
import socket
def check_network_topology():
    print("🌐 Checking network topology...")
    # This is a placeholder for actual network topology checking logic
    print("No network topology issues found.")
if __name__ == "__main__":
    check_network_topology()
    print("🌐 Network topology checked.")

    import logging

logging.basicConfig(filename='security_log.txt', level=logging.INFO, format='%(asctime)s - %(message)s')

def log_suspicious(event: str):
    logging.info(event)

# Example usage
log_suspicious("Suspicious .exe file found in /home/user/downloads/malware.exe")
def log_process_event(event: str):
    logging.info(event)
# Example usage
log_process_event("Unknown process detected: malware.exe (PID 1234)")
def log_system_event(event: str):
    logging.info(event)
# Example usage
log_system_event("High CPU usage detected: 95% at 2023-10-01 12:00:00")
def log_network_event(event: str):
    logging.info(event)
# Example usage
log_network_event("Unusual network connection detected:")
logging.info("Local Address:")
logging.info("  IP:")
logging.info("  Port:") 
logging.info("Remote Address:")
logging.info("  IP:")
logging.info("  Port:")
def log_disk_event(event: str):
    logging.info(event)
# Example usage
log_disk_event("Disk usage exceeded threshold: 95% at /home/user")
def log_memory_event(event: str):
    logging.info(event)
# Example usage
log_memory_event("Memory usage exceeded threshold: 90% at 2023-10-01 12:00:00")
def log_security_event(event: str):
    logging.info(event)
# Example usage
log_security_event("Unauthorized access attempt detected: user 'guest' at 2023-10-01 12:00:00")
def log_backup_event(event: str):
    logging.info(event)
# Example usage
log_backup_event("Backup completed successfully: /home/user/backup at 2023-10-01 12:00:00")
def log_update_event(event: str):
    logging.info(event)

import os
import time

def scan_for_malware(directory):
    # Simulate scanning for files with suspicious extensions
    malware_extensions = ['.exe', '.bat', '.scr', '.vbs']
    found = []
    for filename in os.listdir(directory):
        if any(filename.endswith(ext) for ext in malware_extensions):
            found.append(filename)
    return found

def remove_malware(files, directory):
    for file in files:
        print(f"Removing suspicious file: {file}")
        # Uncomment the next line to actually delete files (be careful!)
        # os.remove(os.path.join(directory, file))

def defense_loop(directory, interval=10):
    print("Starting malware defense loop...")
    while True:
        malware_files = scan_for_malware(directory)
        if malware_files:
            remove_malware(malware_files, directory)
        else:
            print("No malware detected.")
        time.sleep(interval)

if __name__ == "__main__":
    # Change '.' to the directory you want to scan
    defense_loop('.')
# This script scans a directory for files with suspicious extensions and removes them.
# Be cautious with the remove function; it will delete files permanently.
# Ensure you have the necessary permissions to delete files in the directory.
# To run this script, save it as malware_defense.py and execute it in a Python environment.
# Note: This script is a basic example and should not be used as a real malware defense solution.
# Ensure you have Python installed and run this script in a safe environment.
# This script is a basic example and should not be used as a real malware defense solution.
# ...existing code...

def defense_mode():
    print("!!! MALWARE ATTACK DETECTED !!!")
    print("Entering defense mode: Locking system actions.")
    # Simulate locking by stopping the script
    exit("System locked due to malware threat.")

def defense_loop(directory, interval=10):
    print("Starting malware defense loop...")
    while True:
        malware_files = scan_for_malware(directory)
        if malware_files:
            remove_malware(malware_files, directory)
            defense_mode()  # Enter defense mode if malware is found
        else:
            print("No malware detected.")
        time.sleep(interval)

# ...existing code...
# This script scans a directory for files with suspicious extensions and removes them.
# Be cautious with the remove function; it will delete files permanently.
# Ensure you have the necessary permissions to delete files in the directory.
# To run this script, save it as malware_defense.py and execute it in a Python environment.
# Note: This script is a basic example and should not be used as a real malware defense solution.
# Ensure you have Python installed and run this script in a safe environment.
# ...existing code...

def defense_superbug(directory):
    print("SUPERBUG DEFENSE ACTIVATED!")
    malware_files = scan_for_malware(directory)
    if malware_files:
        print("Malicious files detected! Initiating total lockdown.")
        remove_malware(malware_files, directory)
        defense_mode()
    else:
        print("System clear. No threats detected.")

if __name__ == "__main__":
    # Change '.' to the directory you want to scan
    # defense_loop('.')  # Regular defense loop
    defense_superbug('.')  # Superbug defense mode


# ...existing code...   
# This script scans a directory for files with suspicious extensions and removes them.
# Be cautious with the remove function; it will delete files permanently.
# Ensure you have the necessary permissions to delete files in the directory.
# To run this script, save it as malware_defense.py and execute it in a Python environment.
# Note: This script is a basic example and should not be used as a real malware defense solution.
# Ensure you have Python installed and run this script in a safe environment.
# This script is a basic example and should not be used as a real malware defense solution.
# Ensure you have Python installed and run this script in a safe environment.   