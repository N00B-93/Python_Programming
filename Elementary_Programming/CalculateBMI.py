from math import pow

"""
    This is a program that prompts
    the user to enter a weight in pounds and height in inches and displays the BMI.
"""

# Reads in the weight.
weight = float(input("\nEnter your weight in pounds: "))

# Reads in the height.
height = float(input("\nEnter your height in inches: "))

# Calculates the BMI by converting the weight from pounds to kg and the height from inches to meters.
bmi = (weight * 0.45359237) / (pow(height * 0.0254, 2))

# Displays the result.
print(f"\nBMI is {bmi:.2f}")
