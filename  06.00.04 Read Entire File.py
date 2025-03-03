# Open a file for reading
demotextfile = open("06.00.00 DemoText.txt", "r")
# Read the entire contents of the file into a single string
x = demotextfile.read()
# Print the contents - Note the embedded linefeeds
print(x)
# Close the file
demotextfile.close()