import re

# Function to parse the degree string and extract degrees, minutes, and seconds
def ParseDegreeString(ddmmss):
    # Define degree, minute, and second symbols
    degree_symbol = chr(176)  # Unicode for the degree symbol '°'
    minute_symbol = "'"
    second_symbol = '"'
    
    # Find the positions of degree, minute, and second symbols
    degree_pos = ddmmss.find(degree_symbol)
    minute_pos = ddmmss.find(minute_symbol)
    second_pos = ddmmss.find(second_symbol)
    
    # Extract degrees, minutes, and seconds from the string
    degrees = float(ddmmss[:degree_pos].strip())  # Degrees are before the degree symbol
    minutes = float(ddmmss[degree_pos + 1:minute_pos].strip())  # Minutes between degree and minute symbols
    seconds = float(ddmmss[minute_pos + 1:second_pos].strip())  # Seconds between minute and second symbols
    
    return degrees, minutes, seconds

# Function to convert degrees, minutes, and seconds to decimal degrees
def DDMMSStoDecimal(degrees, minutes, seconds):
    # Convert to decimal degrees: degrees + minutes/60 + seconds/3600
    decimal_degrees = degrees + (minutes / 60) + (seconds / 3600)
    return decimal_degrees

# Function to read input file, process angles, and write output file
def convertAngles(input_file, output_file):
    record_count = 0  # To count how many records are processed
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        # Read each line in the input file
        for line in infile:
            line = line.strip()  # Remove any surrounding whitespace
            if line:  # Skip empty lines
                # Parse the angle string into degrees, minutes, and seconds
                degrees, minutes, seconds = ParseDegreeString(line)
                
                # Convert to decimal degrees
                decimal_degrees = DDMMSStoDecimal(degrees, minutes, seconds)
                
                # Write the result to the output file
                outfile.write(f"{decimal_degrees:.12f}\n")  # Write with high precision for correctness
                record_count += 1

    # Print the number of records processed
    print(f"{record_count} records processed")

# Example usage
input_filename = '07.Project Angles Input.txt'
output_filename = '07.Project Angles Output.txt'
convertAngles(input_filename, output_filename)

print(f"Conversion complete. Check the output in {output_filename}.")
