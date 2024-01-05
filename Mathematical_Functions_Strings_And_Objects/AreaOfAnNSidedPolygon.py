from math import pow, tan, pi

"""
    This is a program that prompts the user to enter the
    number of sides and their length of a regular polygon and displays its area.
"""

# Reads in the number of sides of the polygon.
numberOfSides = int(input("\nEnter the number of sided: "))

# Reads in the length of a side.
lengthOfSide = float(input("\nEnter the length of the side: "))

# Calculates the area.
area = numberOfSides * pow(lengthOfSide, 2) / (4 * tan(pi / numberOfSides))

# Displays the result.
print(f"\nThe area of the regular polygon with {numberOfSides} sides is: {area:.2f}")
