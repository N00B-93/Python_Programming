from math import sqrt

"""
    This is a module that contains the functions isValid() which determines if a triangle is a valid triangle and
    area() that determines the rear of a triangle.
"""


def isValid(side1, side2, side3):
    """
     Checks if a triangle is valid by comparing the sum of two sides with the other side.

     :param side1: (float) The first side.

     :param side2: (f;oat) The second side.

     :param side3: (float) The third side.

     :return: bool
     """

    if side1 + side2 < side3 or side1 + side3 < side2 or side2 + side3 < side1:
        return False
    return True


def area(side1, side2, side3):
    """
    Calculates the area of a triangle given three sides.

    :param side1: (float) The first side.

    :param side2: (float) The second side.

    :param side3: (float) The third side.

    :return: (float) The area of the triangle.
    """

    halfPerimeter = (side1 + side2 + side3) / 2

    areaOfTriangle = sqrt(halfPerimeter * (halfPerimeter - side1) * (halfPerimeter - side2) * (halfPerimeter - side3))

    return areaOfTriangle
