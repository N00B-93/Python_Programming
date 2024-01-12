from math import pow, sqrt

"""
    This is a program that prompts the user to enter
    a point (x, y) and checks whether the point is within the rectangle centered at
    (0, 0) with width 10 and height 5.
"""

# Prompts the user to enter the x and y coordinate of a point.
xCoord, yCoord = eval(input("\nEnter the x and y coordinates of the point separated by comma: "))

# Initializes the height and width of the rectangle.
heightOfRectangle = 5
widthOfRectangle = 10

# Calculates the length of half of the Diagonal.
halfDiagonalLength = sqrt(pow(heightOfRectangle / 2, 2) + pow(widthOfRectangle / 2, 2))

# Calculates the distance between the point and the center of the rectangle.
distance = sqrt(pow(xCoord - 0, 2) + pow(yCoord - 0, 2))

if distance < halfDiagonalLength:  # Checks if the point is in the rectangle.
    print(f"\n{(xCoord, yCoord)} is in the rectangle.")
elif distance == halfDiagonalLength:  # Checks if the point is on the rectangle.
    print(f"\n{(xCoord, yCoord)} is on the rectangle.")
else:  # Checks if the point is not in the rectangle.
    print(f"\n{(xCoord, yCoord)} is outside the rectangle.")
