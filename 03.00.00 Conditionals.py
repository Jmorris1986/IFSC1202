x = int(input("Enter a value:"))
if x > 0:
    print(x)
else:
    print(-x)

    x = int(input("Enter a value"))
    if x < 0:
        x = -x
        print(x)

        x = int(input("Enter X value: "))
y = int(input("Enter Y value: "))
if x > 0:
    if y > 0:
        # x is greater than 0, y is greater than 0
        print("Quadrant I")
    else:    
        # x is greater than 0, y is less or equal than 0
        print("Quadrant IV")
else:
    if y > 0:
        # x is less or equal than 0, y is greater than 0
        print("Quadrant II")
    else:    
        # x is less or equal than 0, y is less or equal than 0
        print("Quadrant III")

        print(2 < 5)        # Prints 'True'
print(2 > 5)        # Prints 'False'

print(bool(-10))    # True
print(bool(0))      # False - zero is the only false number
print(bool(10))     # True
print(bool(''))     # False - empty string is the only false string
print(bool('abc'))  # True

a = int(input("Enter First Value: "))
b = int(input("Enter Second Value: "))
if a % 10 == 0 or b % 10 == 0:    
    print('YES')
else:
    print('NO')

    x = int(input("Enter X value: "))
y = int(input("Enter Y value: "))
if x > 0 and y > 0:
    print("Quadrant I")
elif x > 0 and y < 0:    
    print("Quadrant IV")
elif y > 0:    
    print("Quadrant II")
else:
    print("Quadrant III")