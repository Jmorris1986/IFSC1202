# Function to perform the calculation based on the operator
def calculate(operand1, operand2, operator):
    if operator == '+':
        return operand1 + operand2
    elif operator == '-':
        return operand1 - operand2
    elif operator == '*':
        return operand1 * operand2
    elif operator == '/':
        if operand2 != 0:
            return operand1 / operand2
        else:
            return "Error: Division by zero"
    else:
        return "Invalid Operator"

# Prompt the user for the first operand
operand1 = float(input("Enter the first operand (number): "))

# Prompt the user for the operator
operator = input("Enter an operator (+, -, *, /): ")

# Prompt the user for the second operand
operand2 = float(input("Enter the second operand (number): "))

# Perform the calculation
result = calculate(operand1, operand2, operator)

# Display the result
if result == "Invalid Operator":
    print(result)
elif result == "Error: Division by zero":
    print(result)
else:
    print(f"{operand1} {operator} {operand2} = {result}")
