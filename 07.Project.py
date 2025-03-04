def ParseDegreeString(ddmmss):
    # Find the positions of the degree, minute, and second symbols
    degree_pos = ddmmss.find(chr(176))
    minute_pos = ddmmss.find("'")
    second_pos = ddmmss.find('"')
    
    # Extract degrees, minutes, and seconds from the string
    degrees = float(ddmmss[:degree_pos])
    minutes = float(ddmmss[degree_pos + 1:minute_pos])
    seconds = float(ddmmss[minute_pos + 1:second_pos])
    
    return degrees, minutes, seconds

def DDMMSStoDecimal(degrees, minutes, seconds):
    # Convert degrees, minutes, and seconds to decimal degrees
    decimal_degrees = degrees + (minutes / 60) + (seconds / 3600)
    return decimal_degrees

def convert_file(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        count = 0
        for line in infile:
            ddmmss = line.strip()
            degrees, minutes, seconds = ParseDegreeString(ddmmss)
            decimal_degrees = DDMMSStoDecimal(degrees, minutes, seconds)
            outfile.write(f"{decimal_degrees}\n")
            count += 1
        print(f"{count} records processed")

# Example usage
input_file = '07.Project Angles Input.txt'
output_file = '07.Project Angles Output.txt'
convert_file(input_file, output_file)
