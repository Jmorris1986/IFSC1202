number = int(input("Enter a number"))
ones_digit = number % 10
tens_digit = (number - ones_digit)//10
print(f"ones digit: {ones_digit}")
print(f"tens digit: {tens_digit}")