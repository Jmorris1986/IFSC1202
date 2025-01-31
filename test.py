print("HEllo World")
# Constants for time conversion
SECONDS_IN_MINUTE = 60
SECONDS_IN_HOUR = 60 * SECONDS_IN_MINUTE
SECONDS_IN_DAY = 24 * SECONDS_IN_HOUR
SECONDS_IN_YEAR = 365 * SECONDS_IN_DAY

# Prompt for the length of time in seconds
total_seconds = int(input("Enter Length of Time in Seconds: "))

# Calculate the number of years
years = total_seconds // SECONDS_IN_YEAR
remaining_seconds = total_seconds % SECONDS_IN_YEAR

# Calculate the number of days
days = remaining_seconds // SECONDS_IN_DAY
remaining_seconds %= SECONDS_IN_DAY

# Calculate the number of hours
hours = remaining_seconds // SECONDS_IN_HOUR
remaining_seconds %= SECONDS_IN_HOUR

# Calculate the number of minutes
minutes = remaining_seconds // SECONDS_IN_MINUTE
remaining_seconds %= SECONDS_IN_MINUTE

# The remaining seconds
seconds = remaining_seconds

# Display the results
print(f"Years: {years}")
print(f"Days: {days}")
print(f"Hours: {hours}")
print(f"Minutes: {minutes}")
print(f"Seconds: {seconds}")
