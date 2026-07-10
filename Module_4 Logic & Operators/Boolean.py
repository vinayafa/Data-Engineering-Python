# Boolean values are True and False.
print(True)
print(False)

# type(True) shows the data type of a boolean value.
print(type(True))

# bool() converts values to True or False based on truthiness.
print(bool(123))
print(bool("Hi"))
print(bool())
print(bool(0))
print(bool(""))
print(bool(None))

# Now some built-in boolean helper functions.

# any() returns True if at least one value in the list is truthy.
email = ""
phone = "0176-123456"
username = ""
# Allows registration if any field is filled.
print(any([email, phone, username]))


# If all values are empty, any() returns False.
email = ""
phone = ""
username = ""
# Allows registration if any field is filled.
print(any([email, phone, username]))


# all() returns True only when every value in the list is truthy.
email = ""
phone = "0176-123456"
username = ""
# Allows registration only if all fields are filled.
print(all([email, phone, username]))


email = "tillu@1234.com"
phone = "0176-123456"
username = "bananananana"
# Allows registration only if all fields are filled.
print(all([email, phone, username]))


# isinstance(value, type) checks whether a value belongs to a specific type.
print(isinstance(123, int))
print(isinstance(True, str))

# endswith() checks whether a string ends with the given text.
print("Hello".endswith("o"))

# startswith() checks whether a string begins with the given text.
print("Hello".startswith("o"))

# Definition: booleans represent True/False values, bool() checks truthiness, any() needs one truthy item, all() needs all truthy items, and isinstance() checks a value’s type.