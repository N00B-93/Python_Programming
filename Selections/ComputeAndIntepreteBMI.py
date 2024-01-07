from math import pow

"""
    Body Mass Index (BMI) is a measure of health based on height and weight. It can be calculated
    by taking your weight in kilograms and dividing it by the square of your height in
    meters. This is a program that prompts the user to enter a weight in pounds and height in feet and inches then
    displays the BMI. Note that one pound is 0.45359237 kilograms and one inch is 0.0254
    meters.
"""

# Conversion constants
KILOGRAMS_PER_POUND = 0.45359237
METERS_PER_INCH = 0.0254
FEET_TO_METERS = 0.305

# Prompts the user to enter weight in pounds and height in feet and inches.
weight = float(input("\nEnter your weight in pounds: "))
feet = float(input("\nEnter feet: "))
inches = float(input("\nEnter inches: "))

# Converts weight from pounds to kg and height from feet and inches to meters.
weightInKg = weight * KILOGRAMS_PER_POUND
heightInMeters = feet * FEET_TO_METERS
inchesToMeters = inches * METERS_PER_INCH

# Determines the new height in meters.
height = heightInMeters + inchesToMeters

# Calculates the BMI.
bmi = weightInKg / (pow(height, 2))

# Displays the user's BMI Status based on the calculated BMI value.
if bmi < 18.5:
    print("\nUnderweight")
elif 18.5 <= bmi <= 24.9:
    print("\nNormal")
elif 24.9 < bmi <= 29.9:
    print("\nOverweight")
elif 30 > bmi:
    print("\nObese")
