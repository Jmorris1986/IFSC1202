def convert_to_seconds(hours, minutes, seconds):
    return hours * 3600 + minutes * 60 + seconds

# Get the first timestamp
first_hours = int(input("Enter Hours for first timestamp: "))
first_minutes = int(input("Enter Minutes for first timestamp: "))
first_seconds = int(input("Enter Seconds for first timestamp: "))

# Get the second timestamp
second_hours = int(input("Enter Hours for second timestamp: "))
second_minutes = int(input("Enter Minutes for second timestamp: "))
second_seconds = int(input("Enter Seconds for second timestamp: "))

# Convert both timestamps to total seconds
first_total_seconds = convert_to_seconds(first_hours, first_minutes, first_seconds)
second_total_seconds = convert_to_seconds(second_hours, second_minutes, second_seconds)

# Calculate the difference
time_difference = second_total_seconds - first_total_seconds

print(f"The difference is {time_difference} seconds.")
