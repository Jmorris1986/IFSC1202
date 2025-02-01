number = int(input("Enter a number"))
tens_digit = (number // 10)
ones_digit = number % 10
swapped_number = (ones_digit * 10) + tens_digit

print(f"swapped number: {swapped_number}")