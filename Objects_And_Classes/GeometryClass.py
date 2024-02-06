from math import tan, pi

"""
    This is a program that creates three Regular Polygon objects, created using NSidedPolygon(),
    using NSidedPolygon(6, 4) and NSidedPolygon(10, 4, 5.6, 7.8). For
    each object, display its perimeter and area.
"""


class NSidedPolygon:
    """
    A class representing an NSided polygon.

    Attributes:
        numberOfSides -(int) The number of sides of the polygon.

        lengthOfSide (float) The length of the sides of the polygon.

        xCoord (float) The x coordinate of the center of the polygon.

        yCoord (float) The y coordinate of the center of the polygon.
    """

    def __init__(self, numberOfSides=3, lengthOfSide=1, xCoord=0.0, yCoord=0.0):
        self.__numberOfSides = numberOfSides
        self.__lengthOfSide = lengthOfSide
        self.__xCoord = xCoord
        self.__yCoord = yCoord

    def getNumberOfSides(self):
        """
        Returns the number of sides of the polygon.

        :return: (int) The number of sides of the polygon.
        """
        return self.__numberOfSides

    def setNumberOfSides(self, numberOfSides):
        """
        Sets the number of sides of the polygon to the given.

        :param numberOfSides: (int) The number of sides of the polygon.

        :return: None.
        """
        self.__numberOfSides = numberOfSides

    def getLengthOfSides(self):
        """
        Returns the length of the sides of the polygon.

        :return: (float) The length of the sides of the polygon.
        """
        return self.__lengthOfSide

    def setLengthOfSide(self, lengthOfSide):
        """
        Sets the length of the sides of the polygon to the given length.

        :param lengthOfSide: (float) The length of the sides of the polygon.

        :return: None
        """
        self.__lengthOfSide = lengthOfSide

    def getXCoord(self):
        """
        Returns the x coordinate of the center of the polygon.

        :return: (float) The x coordinate of the center of the polygon.
        """
        return self.__xCoord

    def setXCoord(self, xCoord):
        """
        Sets the x coordinate of the center of the polygon to the given xCoord.

        :param xCoord: (float) The x coordinate of the center of the polygon.

        :return: None.
        """
        self.__xCoord = xCoord

    def getYCoord(self):
        """
        Returns the y coordinate of the center of the polygon.

        :return: (float) The y coordinate of the center of the polygon.
        """
        return self.__yCoord

    def setYCoord(self, yCoord):
        """
        Sets the y coordinate of the center of the polygon to the given.

        :param yCoord: (float) The y coordinate of the center of the polygon.

        :return: None.
        """
        self.__yCoord = yCoord

    def getPerimeter(self):
        """
        Returns the perimeter of the polygon.

        :return: (float) The perimeter of the polygon.
        """
        return self.__lengthOfSide * self.__numberOfSides

    def getArea(self):
        """
        Returns the area of the polygon.

        :return: (float) The area of the polygon.
        """
        return (self.__numberOfSides * self.__lengthOfSide ** 2) / (4 * tan(pi / self.__numberOfSides))


def main():
    # Creates two NSidedPolygon Objects.
    nSidedPolygon1 = NSidedPolygon(6, 4)
    nSidedPolygon2 = NSidedPolygon(10, 4, 5.6, 7.8)

    # Displays the properties of the first polygon.
    print("\n\t\tnSidedPolygon1")
    print(f"Area: {format(nSidedPolygon1.getArea(), '.2f')}\nPerimeter: {nSidedPolygon1.getPerimeter()}")

    # Displays the properties of the second polygon.
    print("\n\t\tnSidedPolygon2")
    print(f"Area: {format(nSidedPolygon2.getArea(), '.2f')}\nPerimeter: {nSidedPolygon2.getPerimeter()}")


if __name__ == "__main__":
    main()
