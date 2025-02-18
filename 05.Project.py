def count_digits(n):
    count = 0
    temp = n
    while temp > 0:
        temp //= 10
        count += 1
    return count

def is_special_number(n):
    num_digits = count_digits(n)
    temp = n
    sum_of_powers = 0
    while temp > 0:
        digit = temp % 10
        sum_of_powers += digit ** num_digits
        temp //= 10
    return sum_of_powers == n

def find_special_numbers(start, end):
    for num in range(start, end + 1):
        if is_special_number(num):
            print(num)

start_range = int(input("Enter start of range: "))
end_range = int(input("Enter end of range: "))
find_special_numbers(start_range, end_range)