from math import tan, pow, pi

"""
    This is a program that prompts the user to enter the length of the side of a pentagon and displays
    the area.
"""

lengthOfSide = float(input("\nEnter the length of the side: "))

area = 5 * pow(lengthOfSide, 2) / (4 * tan(pi / 5))

print(f"\nThe area of the pentagon is: {area:.2f}")
