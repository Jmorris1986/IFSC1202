# Function to calculate the product of 5 numbers
def calculate_product(numbers):
    product = 1
    for num in numbers:
        product *= num
    return product

# Input: Prompt the user to enter 5 numbers
print("Enter 5 numbers to calculate their product:")
numbers = []

for i in range(5):
    while True:
        try:
            number = float(input(f"Enter number {i + 1}: "))
            numbers.append(number)
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Calculate the product
result = calculate_product(numbers)

# Output: Display the result
print(f"The product of the entered numbers is: {result}")