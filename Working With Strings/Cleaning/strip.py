# lstrip() removes spaces from the left side of the string.
text = " Engineering".lstrip()
print(text)


# rstrip() removes spaces from the right side of the string.
text = "Engineering   ".rstrip()
print(text)


# strip() removes spaces from both the left and right sides.
text = "                 Engineering                 ".strip()
print(text)

# strip() can also remove a specific character from both ends.
text = "Data enginering".strip()

# Here strip("#") removes # symbols from both sides.
text = "#####ENGINEERING".strip("#")
print(text)

# Remove extra spaces and check how many were present.
text = " Engineering "
print(len(text.strip()))
number_of_spaces = len(text) - len(text.strip())
is_clean = len(text) == len(text.strip())
print("Number of Spaces:", number_of_spaces)
print("Is my data clean?", is_clean)


# When the string has no extra spaces, strip() does not change it.
text = "Engineering"
print(len(text.strip()))
number_of_spaces = len(text) - len(text.strip())
is_clean = len(text) == len(text.strip())
print("Number of Spaces:", number_of_spaces)
print("Is my data clean?", is_clean)