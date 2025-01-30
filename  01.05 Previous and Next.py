# Prompt the user to enter an integer
number = int(input("Enter Number: "))

# Calculate the next and previous numbers
next_number = number + 1
previous_number = number - 1

# Print the results as specified
print("The next number for the number " + str(number) + " is " + str(next_number) + ".")
print("The previous number for the number " + str(number) + " is " + str(previous_number) + ".")
