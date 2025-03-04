# Input integer N
N = int(input("Enter the number of steps (N ≤ 9): "))

# Outer loop for each step
for i in range(1, N + 1):
    # Inner loop to print integers from 1 to i
    for j in range(1, i + 1):
        print(j, end='')  # Print numbers without spaces
    print()  # Newline after each step
