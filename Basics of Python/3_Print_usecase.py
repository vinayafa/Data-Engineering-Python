# This file demonstrates using print() with calculations and variables.
price_shirt = 25.00      # price of one shirt in rupees
price_jeans = 45.50      # price of one pair of jeans

qty_shirt = 2            # number of shirts being bought
qty_jeans = 1            # number of jeans being bought

total_shirt = price_shirt * qty_shirt
total_jeans = price_jeans * qty_jeans
subtotal = total_shirt + total_jeans
print("Subtotal:", subtotal)     # display the subtotal

discount = subtotal * 0.10      # calculate 10% discount
print("Discount:", discount)    # show the discount amount

final_total = subtotal - discount
print("Final Total:", final_total)  # show the final payable amount

# print() is a built-in Python function.
# It is used to display information or debug values.

