# Escape sequences let you include special characters in strings.
# Use backslashes to escape quotes, new lines, tabs, and backslashes.

print("Hi \"Python\"")  # print quotes inside a string
print('hi\'python\'')      # another way to print quotes
print("Path: C:\\User\\Vinay")  # print a Windows-style file path

print("Message1 \n\n\n\nMessage2")  # \n creates a new line
print("Message1\tMessage2")            # \t inserts a tab

# Assignment answer: use escape sequences to format a list.
print("Your Learning Path:\n\t-Python Basics \n\t-Data Engineering \n\t-AI")

# Same output using a multiline string with triple quotes.
print("""Your Learning Path:
\t-Python Basics
\t-Data Engineering
\t-AI""")
