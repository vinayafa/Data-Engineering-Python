# This file shows common numeric data types in Python.

# int is a whole number.
x = 5

# float is a decimal number.
y = 5.7

# complex numbers have a real part and an imaginary part.
z = 22 + 3j

# This is a string, not a number yet.
a = "24"

# type() tells us the data type of a value.
print(type(x))
print(type(y))
print(type(z))
print(type(a))

# int() converts a string containing digits into a whole number.
a = int(a)
print(type(a))

# int() removes the decimal part and keeps only the whole number.
x = 3.14
print(int(x))

# float() converts a whole number into a decimal number.
x = 3
print(float(x))

# complex(real, imaginary) creates a complex number.
x = 3  # real part
y = 4  # imaginary part
print(complex(x, y))

# Definition: type() returns the data type of a value, int() converts to a whole number, float() converts to a decimal number, and complex() creates a complex number.