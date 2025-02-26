# Open the file for writing
newfile = open("06.00.00 OutputText.txt", "w")
# Output 10 numbers
for i in range(1,11):
# Note output does not contain a linefeed character,
# so we will have to add a linefeed when we write it it.
	output = "The number is " + str(i)
	newfile.write(output + "\n")
# Close the file
newfile.close()
print("File Created")