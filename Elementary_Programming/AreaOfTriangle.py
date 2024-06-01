from math import sqrt, pow

"""
    This is a program that prompts the user to enter the
    coordinates (x1, y1), (x2, y2), and (x3, y3) of the vertices of a triangle and displays its area.
"""

# Reads in the co-ordinate of each side of the triangle.
x1, y1 = eval(input("\nEnter the first point (x1, y1) separated by comma: "))
x2, y2 = eval(input("\nEnter the second point (x2, y2) separated by comma: "))
x3, y3 = eval(input("\nEnter the third point (x3, y3) separated by comma: "))

# Determines the length of each side by calculating the distance between each point.
side1 = sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2))
side2 = sqrt(pow(x2 - x3, 2) + pow(y2 - y3, 2))
side3 = sqrt(pow(x1 - x3, 2) + pow(y1 - y3, 2))

# Calculates the perimeter of the triangle.
perimeter = (side1 + side2 + side3) / 2

# Calculates the area using Hero's Formula.
area = sqrt(perimeter * (perimeter - side1) * (perimeter - side2) * (perimeter - side3))

# Displays the result.
print(f"\nThe area of the triangle is: {area:.2f}")
