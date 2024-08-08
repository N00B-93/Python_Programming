from math import pow

"""
    This is a program that prompts
    the user to enter a weight in pounds and height in inches and displays the BMI.
"""

# Reads in the weight.
weight = float(input("\nEnter your weight in pounds: "))

# Reads in the height.
height = float(input("\nEnter your height in inches: "))

# Constants used to convert weight from lbs to kg and length from in to m.
POUNDS_TO_KILOGRAM = 0.45359237
INCHES_TO_METERS = 0.0254

# Calculates the BMI by converting the weight from pounds to kg and the height from inches to meters.
bmi = (weight * POUNDS_TO_KILOGRAM) / (pow(height * INCHES_TO_METERS, 2))

# Displays the result.
print(f"\nBMI is {bmi:.2f}")
