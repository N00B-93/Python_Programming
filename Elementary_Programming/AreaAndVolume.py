from math import pi

"""
    This is a program that reads in the radius and length of a cylinder
    and then calculate and displays the area and volume of the cylinder.
"""

# Takes radius from the user.
radius = float(input("\nEnter the radius of the cylinder: "))

# Takes length from the user.
length = float(input("\nEnter the length of the cylinder: "))

# Calculates the area.
area = pi * radius ** 2

# Calculates the volume.
volume = pi * length * radius ** 2

# Displays the result.
print(f"\nArea = {area:.2f}\nVolume = {volume:.3f}")
