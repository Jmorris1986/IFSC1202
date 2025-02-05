sum = 0
n = int(input("Enter a number:"))
for i in range(1, n + 1):
    sum += i
    # this ^^ is the shorthand for
    # sum = sum + i
print(sum)