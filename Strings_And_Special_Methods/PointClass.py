from math import pow, sqrt

"""
    This is a program that prompts the user to enter two points, displays the distance between
them, and indicates whether they are near each other.
"""


class Point:
    """
    A class representing points.

    Attributes:
        x (float): The x-coordinate of the Point

        y (float): The y-coordinate of the Point.
    """

    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y

    def getXCoordinate(self):
        """
        Returns the x-coordinate of the Point.

        :return: (float) The x-coordinate of the Point.
        """
        return self.__x

    def getYCoordinate(self):
        """
        Returns the y-coordinate of the Point.

        :return: (float) The y-coordinate of the Point.
        """
        return self.__y

    def distance(self, point):
        """
        Returns the distance between two Point Objects.

        :param point: (Point) The second Point Object.

        :return: (float) The distance between the two points.
        """
        return sqrt(pow(self.__x - point.getXCoordinate(), 2) + pow(self.__y - point.getYCoordinate(), 2))

    def isNearBy(self, point):
        """
        Checks if two Point Objects are near each other.

        :param point: (Point) The second Point Object.

        :return: (bool) True if the two Point Objects are near each other otherwise False.
        """
        return self.distance(point) < 5.0

    def __str__(self):
        """
        Returns a string representation of the Point Object.

        :return: (str) The string representation of the Point Object in the form (x, y).
        """
        return f"({self.getXCoordinate(), self.getYCoordinate()})"


def main():
    # Reads in the x and y coordinates of the first point.
    x1 = float(input("\nEnter the x-coordinate of the first Point: "))
    y1 = float(input("\nEnter the y-coordinate of the first Point: "))

    x2 = float(input("\nEnter the x-coordinate of the second Point: "))
    y2 = float(input("\nEnter the y-coordinate of the second Point"))

    # Creates two Point Objects.
    point1 = Point(x1, y1)
    point2 = Point(x2, y2)

    # Displays the result.
    print(f"\nThe distance between point1 and point2 is: {point1.distance(point2):.2f}")
    print(f"\nIs point1 near point2? {point1.isNearBy(point2)}")


if __name__ == "__main__":
    main()
