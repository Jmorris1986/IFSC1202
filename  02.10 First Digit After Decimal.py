def first_decimal_digit (number):
    decimal_part = abs (number) % 1
    first_digit= int(decimal_part * 10)

    print(first_digit)
number = float(input("enter a number:"))
first_decimal_digit(number)