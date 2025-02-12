for i in range(5, 8):
    print(i, i ** 2)
print('End of Loop')
5, 25
6, 36
7, 49


for i in range(3):
    print(i)

    x = 4
for i in range(x):
    print('Hello, world!')

for i in range(-5):
    print("Hello, world!")
print("End of Loop")


result = 0
n = 5
for i in range(1, n + 1):
    result += i
    # this ^^ is the shorthand for
    # result = result + i
print(result)

for i in range(10, 0, -2):
    print(i)


    print(1, 2, 3)
print(4, 5, 6)
print(1, 2, 3, sep=", ", end=". ")
print(4, 5, 6, sep=", ", end=". ")
print()
print(1, 2, 3, sep="", end=" -- ")
print(4, 5, 6, sep=" * ", end=".")

