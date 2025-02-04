number = int(input("Enter a three digit number: "))
if 100 <= number <= 999:
    hundreds_digit = (number // 100)
    tens_digit = (number // 10) % 10
    ones_digit = number % 10

reversed_number = (ones_digit * 100) + (tens_digit * 10) + hundreds_digit

print(f"reversed number of: {number} is {reversed_number}")

