# Multiple assignment is useful when you need
# to swap the values of two variables.
# In older programming languages
# this can be done using a temporary variable:
a = 1
b = 2
# swap the value in a and b
tmp = a
a = b
b = tmp
print(a, b) # will print '2 1'
# Now use the multiple assignment statement to swap the values
a = 1
b = 2
# In Python, the same swap can be written in one line:
a, b = b, a
print(a, b)
