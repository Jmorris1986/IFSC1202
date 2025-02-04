number = float(input("enter a number"))
fractional_part = number - int(number)
rounded_fraction = round(fractional_part,1)
print(f"fractional part rounded to the nearest tenth: {rounded_fraction}")