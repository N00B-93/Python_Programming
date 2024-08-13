"""
    This is a program that reads in weight in pounds,
    converts it into kilograms and then displays the result.
"""

# Reads in the weight in pounds.
pounds = float(input("\nEnter the weight in pounds: "))

# Constant to convert weight from pounds to kilogram.
POUNDS_TO_KILOGRAMS = 0.454

# Converts the weight to kilograms.
kilogram = pounds * POUNDS_TO_KILOGRAMS

# Displays the result.
print(f"\n{pounds} pounds is {kilogram:.2f} kilograms")
