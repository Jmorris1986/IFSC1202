n = int(input("enter a number"))
length = 0
    length += 1
    n //= 10
    if n == 0:
print('Length is', length)

n = int(input("enter a number"))
length = 0
while n != 0:
    length += 1
    n //= 10
print('Length is', length)