from math import sin, pow, pi, sqrt

"""
    This is a program that prompts the user to enter the
    length from the center of a pentagon to a vertex and computes the area of the pentagon.
"""

# Reads in the length from the center to a vertex.
length = float(input("\nEnter the length from the center to a vertex: "))

# Calculates the length of a side of the pentagon
lengthOfASide = 2 * length * sin(pi / 5)

# Calculates the area of the pentagon using the length of a side.
area = (3 * sqrt(3) / 2) * pow(lengthOfASide, 2)

# Displays the result.
print(f"\nThe area of the pentagon is {area:.2f}")
