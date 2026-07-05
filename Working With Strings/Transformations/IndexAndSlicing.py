text = "Python"

# Indexing starts at 0, so text[0] gives the first character.
print(text[0])

# Negative indexing counts from the end, so -6 also gives the first character.
print(text[-6])

# text[5] gives the last character because "Python" has 6 letters.
print(text[5])

# text[-1] is a common way to get the last character.
print(text[-1])

# text[3] gives the fourth character, which is "h".
print(text[3])


# Slicing lets you extract part of a string using a start and end index.
date = "2026-09-20"

# text[start:end] includes the start index but excludes the end index.
print(date[0:4])

# Omitting the start index means "begin from the start of the string".
print(date[:4])

# This slice gets the month from the date string.
print(date[5:7])

# Omitting the end index means "go to the end of the string".
print(date[8:])