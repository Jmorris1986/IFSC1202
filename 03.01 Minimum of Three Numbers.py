numbers = list(map(float, input("Enter numbers separated by space:")))

smallest = numbers[0]
for numbers in numbers[1:]:
    if numbers < smallest:
        smallest = numbers

print("the smallest number is:", smallest)
