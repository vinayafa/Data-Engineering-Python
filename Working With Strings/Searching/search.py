# Search examples for checking text patterns.

# startswith() checks whether a string begins with a specific value.
phone = "+49-176-12345"
print(phone.startswith("+49"))

# endswith() checks whether a string ends with a specific value.
email = "baraa@gmail.com"
print(email.endswith("gmail.com"))
print(email.endswith("outlook.com"))


# Use endswith() to check file extensions.
file = "data_backup.csv"
print(file.endswith(".csv"))

# Use in to check whether a character or word exists inside a string.
email = "baraagmail.com"
print("@" in email)

# You can also search for parts of a URL or path with in.
url = "https://api.company.com/v1/data"
print("/api" in url)