# This is a regular string concatenation example.
# It is harder to read because we need to keep adding + signs and convert non-string values.
name = "vinay"
age = 25
is_student = True

# This long line works, but it is not very readable.
print("My name is" + name + ", I am " + str(age) + " years old, and student status is " + str(is_student))

# In the next example, we can use an f-string to make the same idea much easier to read.
# The f before the quotes tells Python to replace { } parts with variable values directly.
print(f"My name is{name}, I am {age} years old , and student status is {is_student}.")


# F-strings can also evaluate expressions inside the braces.
print(f"2+3 = {2+3}")


# Use double braces when you want actual curly braces in the output.
print(f"{{This is me Vinay}}")