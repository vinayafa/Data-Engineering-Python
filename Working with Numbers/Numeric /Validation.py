# is_integer() checks whether a float has no decimal part.
x = 7.0
print(x.is_integer())

# This float has a decimal part, so is_integer() returns False.
y = 7.1
print(y.is_integer())

# isinstance(value, type) checks whether a value belongs to a specific type.
x = 70
print(isinstance(x, int))


# This value is a float, so it is not an int.
x = 70.45
print(isinstance(x, int))
print(isinstance(x, float))

# Definition: is_integer() tells you if a float is a whole number, and isinstance() checks whether a value is an instance of a given type.