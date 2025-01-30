# Prompt for the number of kilometers
kilometers = float(input("Enter Kilometers: "))

# Conversion factor from kilometers to miles
kilometers_to_miles = 1 / 1.61

# Calculate the number of miles
miles = kilometers * kilometers_to_miles

# Display the number of miles
print(f"{kilometers} kilometers is approximately {miles} miles.")
