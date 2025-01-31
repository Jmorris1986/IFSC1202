from math import pi
variable = pi
print(f"Using Numeric variable = {variable}")
print(f"|{variable:25}|")
print(f"|{variable:<25}|")
print(f"|{variable:>25}|")
print(f"|{variable:^25}|")
print()
variable = "Python 3.9"
print(f"Using String variable = {variable}")
print(f"|{variable:25}|")
print(f"|{variable:<25}|")
print(f"|{variable:>25}|")
print(f"|{variable:^25}|")

from math import pi
variable = pi
print(f"Using String variable = {variable}")
print(f"|{variable:=<25}|")
print(f"|{variable:=>25}|")
print(f"|{variable:=^25}|")
print()
variable = "Python 3.9"
print(f"Using String variable = {variable}")
print(f"|{variable:=<25}|")
print(f"|{variable:=>25}|")
print(f"|{variable:=^25}|")

import math
variable = 10
print(f"Using Numeric variable = {variable}")
print(f"This prints without formatting {variable}")
print(f"This prints with formatting {variable:d}")
print(f"This prints also with formatting {variable:n}")
print(f"This prints with spacing {variable:10d}")
print()
variable = math.pi
print(f"Using Numeric variable = {variable}")
print(f"This prints without formatting {variable}")
print(f"This prints with formatting {variable:f}")
print(f"This prints with spacing {variable:20f}")

variable = 4
print(f"Using Numeric variable = {variable}")
print(f"This prints without formatting {variable}")
print(f"This prints with percent formatting {variable:%}")
print()
variable = 403267890
print(f"Using Numeric variable = {variable}")
print(f"This prints with exponential formatting {variable:e}")

variable = 1200356.8796
print(f"Using Numeric variable = {variable}")
print(f"With two decimal places: {variable:.2f}")
print(f"With four decimal places: {variable:.3f}")
print(f"With two decimal places and a comma: {variable:,.2f}")
print(f"With a forced plus sign: {variable:+.2f}")
print()
variable *= -1
print(f"Using Numeric variable = {variable}")
print(f"With two decimal places and a comma: {variable:,.2f}")

print(f'{"Number":>10s}{"Square":>10s}{"Cube":>10s}')
x = 1.0
print(f'{x:10.2f}{x*x:10.2f}{x*x*x:10.2f}')
x = 2.0
print(f'{x:10.2f}{x*x:10.2f}{x*x*x:10.2f}')
x = 3.0
print(f'{x:10.2f}{x*x:10.2f}{x*x*x:10.2f}')

APPLES = .50
BREAD = 1.50
CHEESE = 2.25
numApples = 3
numBread = 10
numCheese = 6
prcApples = numApples * APPLES
prcBread = numBread* BREAD
prcCheese = numCheese * CHEESE
strApples = 'Apples'
strBread = 'Rye Bread'
strCheese = 'Cheese'
total = prcBread + prcCheese + prcApples
print(f'{"My Grocery List":^30s}')
print(f'{"="*30}')
print(f'{strApples:10s}{numApples:10d}{"":5s}${prcApples:>5.2f}')
print(f'{strBread:10s}{numBread:10d}{"":5s}${prcBread:>5.2f}')
print(f'{strCheese:10s}{numCheese:10d}{"":5s}${prcCheese:>5.2f}')
print(f'{"":10s}{"Total:":>10s}{"":5s}${total:>5.2f}')
