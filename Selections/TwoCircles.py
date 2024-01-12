from math import pow, sqrt

"""
    This is a program prompts the user to enter the center
    coordinates and radii of two circles and determines whether the second circle is
    inside the first or overlaps with the first.
    Hint: circle2 is inside circle1 if the distance between the two centers <= | r1 - r2| and circle2
    overlaps circle1 if the distance between the two centers <= r1 + r2
"""

# Prompts the user to enter the center coordinates and radii of two circles respectively.
x1, y1, r1 = eval(input("\nEnter the center coordinates and radius of circle1 separated by comma(x1, y1, r1): "))
x2, y2, r2 = eval(input("\nEnter the center coordinates and radius of circle1 separated by comma(x2, y2, r2): "))

# Calculates the distance between their centers.
distance = sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2))

if distance <= abs(r1 -r2):  # Checks if circle1 is in circle2
    print("\nCircle1 is inside Circle2.")
elif distance <= abs(r1 + r2):  # Checks if circle2 overlaps circle1
    print("\nCircle2 overlaps circle1")
else:  # Checks if circle2 is outside circle1
    print("\nCircle2 is outside circle1")

