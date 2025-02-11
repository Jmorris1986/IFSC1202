def check_ascending_order(number):
    # Extract the hundreds, tens, and ones digits
    hundreds = number // 100  # Integer division to get the hundreds place
    tens = (number // 10) % 10  # Integer division by 10 and then modulo 10 to get the tens place
    ones = number % 10  # Modulo 10 to get the ones place
    
    # Check if the digits are in ascending order
    if hundreds < tens < ones:
        print("YES")
    else:
        print("NO")

# Example usage:
number = 654
check_ascending_order(number)
