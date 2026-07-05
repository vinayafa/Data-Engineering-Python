# lower() converts all letters to lowercase.
# upper() converts all letters to uppercase.
text = "python PROGRAMMING "
print(text.lower())
print(text.upper())


# Clean both strings before comparing them.
# lower() makes the text the same case, and strip() removes extra spaces.
search = "Email  ".lower().strip()
data = "  emAil".lower().strip()

# After cleaning, both values match.
print(search == data)