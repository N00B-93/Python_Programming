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

# Prompts the user to enter weight in pounds.
weight = float(input("\nEnter your weight in pounds: "))

# Displays an error message and terminates the program if the weight is <= 0.
if weight <= 0:
    print(f"\nError: Use a weight > 0, Try again.\n")
    exit(1)

# Prompts the user to enter the value for the feet and inches.
feet, inches = eval(input("\nEnter feet and inches separated by comma: "))

# Displays an error message and terminates the program if the feet or inches is <= 0.
if feet <= 0 or inches <= 0:
    print(f"\nError: Use positive values > 0 for feet and inches, Try again.\n")
    exit(2)

# Converts weight from pounds to kg and height from feet and inches to meters.
weightInKg = weight * KILOGRAMS_PER_POUND
heightInMeters = feet * FEET_TO_METERS
inchesToMeters = inches * METERS_PER_INCH

# Determines the new height in meters.
height = heightInMeters + inchesToMeters

# Calculates the BMI.
bmi = weightInKg / (pow(height, 2))

# Displays the user's BMI Status based on the calculated BMI value.
print(f"\nBMI: {bmi:.2f}")
if bmi < 18.5:
    print("You are Underweight")
elif 18.5 <= bmi <= 24.9:
    print("You are Normal")
elif 24.9 < bmi <= 29.9:
    print("You are Overweight")
elif 30 > bmi:
    print("You are Obese")
