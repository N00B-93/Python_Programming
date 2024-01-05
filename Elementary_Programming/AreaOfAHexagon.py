from math import sqrt

"""
    This is a program that prompts the user to enter the
    side of a hexagon and displays its area.
"""

# Reads in the side of the Hexagon.
side = float(input("\nEnter the length of the side of the hexagon: "))

# Calculates the area of the Hexagon.
area = (3 * sqrt(3) / 2) * pow(side, 2)

# Displays the result.
print(f"\nThe area of the hexagon is: {area:.2f}")
