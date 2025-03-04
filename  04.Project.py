# Input the maximum height
height = int(input("Enter maximum height: "))

# First loop for the increasing pattern
for i in range(1, height + 1):
    print('* ' * i)

# Second loop for the decreasing pattern
for i in range(height - 1, 0, -1):
    print('* ' * i)
