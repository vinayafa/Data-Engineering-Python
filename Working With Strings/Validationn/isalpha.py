# Validation examples for checking what kind of text is stored in a string.

country = "USA"

# isalpha() returns True when all characters are letters only.
print(country.isalpha())



# This one contains numbers, so isalpha() returns False.
country = "USA12"
print(country.isalpha())


# isnumeric() returns True when the string contains only numbers.
phone = "+045-123456685"
print(phone.isnumeric())

# This value contains only digits, so it passes the numeric check.
phone = "045123456685"
print(phone.isnumeric())