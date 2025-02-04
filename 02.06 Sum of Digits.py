number =  int(input("Enter a three digit number:"))
if 100 <= 999:
    digit1 = number // 100 # hundreds place
    digit2 = number // 10 % 10 # tens place
    digit3 = number % 10 # ones place

    total = digit1 + digit2 + digit3

    print(f"sum of digits of {number} is {total}")
else:
    print("please enter a vaild three digit number.")