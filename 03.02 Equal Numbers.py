first_number = int(input("Enter First Number: "))
second_number = int(input("Enter Second Number: "))
third_number = int(input("Enter Third Number: "))

# Check for equality
if first_number == second_number == third_number:
    print(3)  # All three numbers are the same
elif first_number == second_number or second_number == third_number or first_number == third_number:
    print(2)  # Two numbers are equal
else:
    print(0)  # All numbers are different