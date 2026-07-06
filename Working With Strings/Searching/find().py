# find() helps locate the position of a character or substring inside a string.

# These phone numbers all have different country-code lengths.
phone1 = "+49-176-12345"
phone2 = "4-176-12345"
phone3 = "0048-345-12341234"


# Manual slicing removes the country code by using a fixed index.
print(phone1[4:])
print(phone2[3:])

# find("-") finds the dash, and +1 starts from the text after it.
print(phone1[phone1.find("-") + 1:])
print(phone2[phone2.find("-") + 1:])
print(phone3[phone3.find("-") + 1:])

# Definition: find() returns the index of the first match, or -1 if the value is not found.