from math import pow, sqrt

"""
    This is a program that prompts the user to enter a
    point (x, y) and checks whether the point is within the circle centered at (0, 0) with radius 10.
"""

# Prompts the user to enter the x and y coordinate of a point.
xCoord, yCoord = eval(input("\nEnter the x and y coordinates of the point separated by comma: "))

# Calculates the distance between the point and the center of a circle centered at the origin.
distance = sqrt(pow(xCoord - 0, 2) + pow(yCoord - 0, 2))

if distance < 10:  # Checks if the point is within the circle.
    print(f"\n{(xCoord, yCoord)} is within the circle.")
elif distance == 10:  # Checks if the point is on the circle.
    print(f"\n{(xCoord, yCoord)} is on the circle.")
else:  # Checks if the point is outside the circle.
    print(f"\n{(xCoord, yCoord)} is outside the circle.")
