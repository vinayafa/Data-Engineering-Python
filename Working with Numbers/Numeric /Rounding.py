import math

# abs() gives the distance from zero, so it is useful when you want to ignore the sign.
print(abs(2 - 10))

# round() is used when we want a number with fewer decimal places.
# This is useful for money, averages, and any value that should look cleaner.
price = 35.52345235

# round(number, 2) keeps 2 decimal places.
print(round(price, 2))

# round(number, 3) keeps 3 decimal places.
print(round(price, 3))

# round(number, 1) keeps 1 decimal place.
print(round(price, 1))

# round(number) without a second argument rounds to the nearest whole number.
print(round(price))

# math.floor() rounds down to the next lower integer.
print(math.floor(price))

# math.ceil() rounds up to the next higher integer.
print(math.ceil(price))

# math.trunc() removes the decimal part without rounding.
print(math.trunc(price))

# int() also removes the decimal part, which is why it is similar to truncation here.
print(int(price))

# Definition: abs() returns the absolute value, round() changes decimal precision, floor() rounds down, ceil() rounds up, trunc() removes decimals, and int() converts to a whole number.
