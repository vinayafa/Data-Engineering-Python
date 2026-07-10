import random

# random.random() returns a random decimal number between 0.0 and 1.0.
# This is useful when you need a random float or want to build probability-based logic.
print(random.random())


# random.randint(a, b) returns a random whole number between a and b, including both ends.
# This is useful for dice rolls, random selections, and simple games.
print(random.randint(1, 6))

# Definition: the random module helps generate random values; random() gives a float from 0.0 to 1.0, and randint() gives a random integer in a chosen range.