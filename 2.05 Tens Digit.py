number = int(input("Enter a number"))
tens_digit = (number // 10) # to only print the digits in the tens column
ones_digit = tens_digit % 10

print(f"tens digit: {ones_digit}")
