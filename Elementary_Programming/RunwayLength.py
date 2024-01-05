from math import pow

"""
    This is a program that prompts the user to enter v in meters/second (m/s) and the
    acceleration a in meters/second squared and displays the minimum runway
    length.
"""

# Reads in the speed v.
speed = float(input("\nEnter the speed: "))

# Reads in the acceleration a.
acceleration = float(input("\nEnter the acceleration: "))

# calculates the runway length.
runwayLength = pow(speed, 2) / (2 * acceleration)

# Displays the result.
print(f"\nThe minimum runway length for this airplane is: {runwayLength:.2f} meters")


