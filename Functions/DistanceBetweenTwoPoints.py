from math import pow, sqrt

"""
    This is a program that calculates the distance between two points
    using a formular with the header;
                def distance(x1, y1, x2, y2):
"""


def distance(x1, y1, x2, y2):
    """
    Calculates the distance between two points

    :param x1: (float) The x-coordinate of the first point.

    :param y1: (float) The y-coordinate of the first point.

    :param x2: (float) The x-coordinate of the second point.

    :param y2: (float) The y-coordinate of the second.

    :return: float: The distance between the two points.
    """

    return sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2))


def main():
    # Reads in the x and y coordinate of each point.
    x1, y1 = eval(input("\nEnter the x and y coordinates of the first point separated by comma(x1, y1): "))

    x2, y2 = eval(input("\nEnter the x and y coordinates of the second point separated by comma(x2, y2): "))

    # Displays the distance between the points.
    print(f"\nThe distance between {(x1, y1)} and {(x2, y2)} is: {distance(x1, y1, x2, y2):.4f}")


if __name__ == "__main__":
    main()
