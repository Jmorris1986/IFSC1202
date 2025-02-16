# Prompt the user to put in the maximum height
height = int(input("enter a maximum height:"))

#Generate the pattern using a loop
for i in range(1, height + 1):
    print('x'* i)