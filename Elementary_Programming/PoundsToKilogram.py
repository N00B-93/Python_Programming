"""
    This is a program that reads in weight in pounds,
    converts it into kilograms and then displays the result.
"""

# Reads in the weight in pounds.
pounds = float(input("\nEnter the weight in pounds: "))

# Converts the weight to kilograms.
kilogram = pounds * 0.454

# Displays the result.
print(f"\n{pounds} pounds is {kilogram:.2f} kilograms")
