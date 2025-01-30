# Prompt for the length of the race in kilometers
race_length_km = float(input("Enter Length of Race in Kilometers: "))

# Prompt for the number of minutes
minutes = int(input("Enter Minutes: "))

# Prompt for the number of seconds
seconds = int(input("Enter Seconds: "))

# Convert the race length from kilometers to miles
race_length_miles = race_length_km / 1.61

# Calculate the total time in hours
total_time_hours = (minutes * 60 + seconds) / 3600

# Calculate the average speed in miles per hour
average_speed_mph = race_length_miles / total_time_hours

# Display the average speed in miles per hour
print(f"Average speed: {average_speed_mph} miles per hour")
