# type() is a built-in function that shows the data type of a value.
name = "Vinay Kumar"
print(type(name))  # <class 'str'>

age = 24
print(type(age))   # <class 'int'>
print("Your age is: " + str(age))  # convert int to string before concatenation

age = age + 5      # add 5 to the integer value
print(age)

age = str(age)      # convert the number to a string
print(type(age))    # <class 'str'>

# Once age is a string, you cannot add an integer to it directly.
# The following line would cause an error if uncommented:
# age = age + 5
# print(age)

# Python is flexible with types, but operations depend on the current data type.
