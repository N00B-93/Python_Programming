"""
    This is a program that reads in length in feet,
    converts it to meters and displays the result.
"""

# Reads in the length in feet.
feet = float(input("\nEnter the length in feet: "))

# Constant to convert feet to meters.
FEET_TO_METERS = 0.305

# Calculates the length in meters.
meter = feet * FEET_TO_METERS

# Displays the result.
print(f"\n{feet} feet is {meter:.2f} meters")
