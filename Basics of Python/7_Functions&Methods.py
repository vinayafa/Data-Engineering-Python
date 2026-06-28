text = "hi"             # string value
number = 10             # integer value

# type() returns the data type of a value.
print(type(text))       # <class 'str'>
print(type(number))     # <class 'int'>

# len() returns the number of characters in a string.
print(len(text))        # output: 2

# String methods only work on strings.
print(text.upper())     # converts text to uppercase

# The next line will raise an error because `number` is an int,
# and integers do not have the string method upper().
# print(number.upper())

# To use string methods, first convert the number to a string:
# print(str(number).upper())
