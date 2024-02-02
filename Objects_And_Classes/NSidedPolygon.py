from math import tan, pi, pow


class NSidedPolygon:
    """
    A class representing an n-sided polygon.

    Attributes:

        n (int): The number of sides.

        side (float): The length of side of the polygon.

        x (float): The x-coordinate of the center of the polygon.

        y (float): The y-coordinate of the center of the polygon.
    """

    def __init__(self, n=3, side=1.0, x=0.0, y=0.0):
        self.__n = n
        self.__side = side
        self.__x = x
        self.__y = y

    def getNumberOfSides(self):
        """
        Returns the number of sides.

        :return: (int) The number of sides.
        """
        return self.__n

    def setNumberOfSides(self, n):
        """
        Sets the number of sides to a given value.

        :param n: (int) The number of sides to set.

        :return: None.
        """
        self.__n = n

    def setLengthOfSides(self, side):
        """
        Sets the length of the given value.

        :param side: (float) The length of a side.

        :return: None.
        """
        self.__side = side

    def getLengthOfSides(self):
        """
        Returns the length of a side.

        :return: (float) The length of a side.
        """
        return self.__side

    def getXCoordinate(self):
        """
        Returns the x coordinate of the centre of the polygon.

        :return: (float) The x coordinate of the centre of the polygon.
        """
        return self.__x

    def getYCoordinate(self):
        """
        Returns the y coordinate of the centre of the polygon.

        :return: (float) The y coordinate of the centre of the polygon.
        """
        return self.__y

    def setXCoordinate(self, x):
        """
        Sets the x coordinate of the centre of the polygon.

        :param x: (float) The x coordinate of the centre of the polygon.

        :return: None
        """
        self.__x = x

    def setYCoordinate(self, y):
        """
        Sets the y coordinate of the centre of the polygon.

        :param y: (float) The y coordinate of the centre of the polygon.

        :return: None.
        """
        self.__y = y

    def getPerimeter(self):
        """
        Returns the perimeter of the polygon.

        :return: (float) The perimeter of the polygon.

        """
        return self.__n * self.__side

    def getArea(self):
        """
        Returns the area of the polygon.

        :return: (float) The area of the polygon.
        """
        return self.__n * pow(self.__side, 2) / (4 * tan(pi / self.__n))


def main():
    # Creates two NSidedPolygon Objects.
    polygon1 = NSidedPolygon(6, 4)
    polygon2 = NSidedPolygon(10, 4, 5.6, 7.8)

    # Displays the polygons areas and perimeters.
    print(f"\n\t\tPolygon1\nPerimeter: {polygon1.getPerimeter():.2f}\nArea: {polygon1.getArea():.2f}")
    print(f"\n\t\tPolygon2\nPerimeter: {polygon2.getPerimeter():.2f}\nArea: {polygon2.getArea():.2f}")


if __name__ == "__main__":
    main()
