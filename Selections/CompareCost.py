"""
    This is a program that prompts the user to enter the weight and price of two different packages of rice, then 
    compares the cost of two packages and displays the one with the better price.
"""

# Reads in the weight and price of the first package.
weight1, price1 = eval(input("\nEnter the weight and price of the first package separated by comma: "))

# Displays an error message and exits the program if the user enters an invalid weight or price.
if weight1 <= 0 or price1 <= 0:
    print("\nError: weight and price should be > 0, Try again.")
    exit(1)

# Reads in the weight and price of the second package.
weight2, price2 = eval(input("\nEnter the weight and price of the second package separated by comma: "))

# Displays an error message and exits the program if the user enters an invalid weight or price.
if weight2 <= 0 or price2 <= 0:
    print("\nError: weight and price should be > 0, Try again.")
    exit(2)

# Calculates the pricePerKg of each package.
pricePerKg1 = price1 / weight1
pricePerKg2 = price2 / weight2

# Displays the package with the better price based on the pricePerKg.
if pricePerKg1 < pricePerKg2:
    print("\nPackage1 has the better price.")
elif pricePerKg1 > pricePerKg2:
    print("\nPackage2 has the better price.")
else:
    print("\nBoth packages have the same price.")
