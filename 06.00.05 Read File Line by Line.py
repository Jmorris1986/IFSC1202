# Open a file for reading
demotextfile = open("06.00.00 DemoText.txt")
# Read the first line of the file
x = demotextfile.readline()
# End of file is indicated when the input is empty
while x != "":
# Print the contents - Note the embedded linefeeds
	print(x)
# Read the next line of the file
	x = demotextfile.readline()
# Close the file
demotextfile.close()