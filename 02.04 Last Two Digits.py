def last_two_digits (number):
   return f"{number % 100:02}"
number = int(input("Enter a number"))

print(f"last two digits: {last_two_digits(number)}")