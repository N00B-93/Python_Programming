from math import sqrt, pow, pi


class Circle2D:
    """
    Class representing a 2-D circle.

    Attributes:
        x (float): The x-coordinate of the center of the circle.

        y (float): The y-coordinate of the center of the circle.

        radius (float): The radius of the circle.
    """
    def __init__(self, x=0, y=0, radius=0):
        self.__x = x
        self.__y = y
        self.__radius = radius

    def getXCoordinate(self):
        """
        Returns the x-coordinate of the center of the circle.

        :return: (float): The x-coordinate of the center of the circle.
        """
        return self.__x

    def getYCoordinate(self):
        """
        Returns the y-coordinate of the center of the circle.

        :return: (float): The y-coordinate of the center of the circle.
        """
        return self.__y

    def getRadius(self):
        """
        Returns the radius of the circle.

        :return: (float): The radius of the circle.
        """
        return self.__radius

    def getArea(self):
        """
        Returns the area of the circle.

        :return: (float): The area of the circle.
        """
        return pi * pow(self.__radius, 2)

    def getPerimeter(self):
        """
        Returns the perimeter of the circle.

        :return: (float): The perimeter of the circle.
        """
        return 2 * pi * self.__radius

    def containsPoint(self, x, y):
        """
        Checks if the given point is inside the circle.

        :param x: (float) The x-coordinate of the point.

        :param y: (float) The y-coordinate of the point.

        :return: (bool) True if the given point is inside the circle else False.
        """
        return sqrt(pow(self.__x - x, 2) + pow(self.__y - y, 2)) < self.__radius

    def contains(self, circle):
        """
        Checks if the given Circle2D Object is inside the current circle instance.

        :param circle: (Circle2D) The circle to check whether it is inside the current Circle2D instance.

        :return: (bool) True if the given circle is inside the current Circle instance else False.
        """
        return (sqrt(pow(self.__x - circle.getXCoordinate(), 2) + pow(self.__y - circle.getYCoordinate(), 2))
                < abs(self.__radius - circle.getRadius()))

    def overlaps(self, circle):
        """
        Checks if the given Circle2D Object is overlaps with the current Circle2D instance.

        :param circle: (Circle2D) The circle to check whether it overlaps with the current Circle2D instance

        :return: (bool) True if the given circle overlaps with the current Circle2D instance else False.
        """
        return (sqrt(pow(self.__x - circle.getXCoordinate(), 2) + pow(self.__y - circle.getYCoordinate(), 2))
                < abs(self.__radius + circle.getRadius()))

    def __contain__(self, another):
        """
        Returns True if this circle is contained in another circle.

        :param another: (Circle2D) The other circle to check whether the current circle instance is contained in it.

        :return: (bool) True if the given circle contains the current Circle2D instance else False.
        """
        return (sqrt(pow(another.getXCoordinate() - self.__x, 2) + pow(another.getYCoordinate() - self.__y, 2))
                < abs(another.getRadius() - self.__radius))

    def __lt__(self, another):
        """
        Returns True if this circle is less than the given circle.

        :param another: (Circle2D) The other circle to compare with the current Circle2D instance.

        :return: (bool) True if the current circle instance is less than the given Circle2D instance else False.
        """
        return self.getRadius() < another.getRadius()

    def __le__(self, another):
        """
        Returns True if this circle is less than or equal to the given circle.

        :param another: (Circle2D) The other circle to compare with the current Circle2D instance.

        :return: (bool) True if the current circle instance is less than or equal to
        the given Circle2D instance else False.
        """
        return self.getRadius() <= another.getRadius()

    def __eq__(self, another):
        """
        Returns True if this circle is equal to the given circle.

        :param another: (Circle2D) The other circle to compare with the current Circle2D instance.

        :return: (bool) True if the current circle instance is equal to
        the given Circle2D instance else False.
        """
        return self.getRadius() == another.getRadius()

    def __ne__(self, another):
        """
        Returns True if this circle is not equal to the given circle.

        :param another: (Circle2D) The other circle to compare with the current Circle2D instance.

        :return: (bool) True if the current circle instance is not equal to
        the given Circle2D instance else False.
        """
        return self.getRadius() != another.getRadius()

    def __gt__(self, another):
        """
        Returns True if this circle is greater than the given circle.

        :param another: (Circle2D) The other circle to compare with the current Circle2D instance.

        :return: (bool) True if the current circle instance is greater than
        the given Circle2D instance else False.
        """
        return self.getRadius() > another.getRadius()

    def __ge__(self, another):
        """
        Returns True if this circle is greater than or equal to the given circle.

        :param another: (Circle2D) The other circle to compare with the current Circle2D instance.

        :return: (bool) True if the current circle instance is greater than or equal to
        the given Circle2D instance else False.
        """
        return self.getRadius() >= another.getRadius()


def main():
    # Reads in the x and y coordinates of the center of two circles and their radii.
    x1, y1, r1 = eval(input("\nEnter the x-coordinate, y-coordinate, and radius of the first circle separated"
                            " by a comma(x1, y1, r1): "))
    x2, y2, r2 = eval(input("\nEnter the x-coordinate, y-coordinate, and radius of the second circle separated"
                            " by a comma(x2, y2, r2): "))

    # Creates two Circle2D Objects.
    circle1 = Circle2D(x1, y1, r1)
    circle2 = Circle2D(x2, y2, r2)

    # Displays the areas of the circles.
    print(f"\nArea of circle1: {circle1.getArea():.2f}")
    print(f"\nArea of circle2: {circle2.getArea():.2f}\n")

    # Displays the perimeters of the circles.
    print(f"\nPerimeter of circle1: {circle1.getPerimeter():.2f}")
    print(f"\nPerimeter of circle2: {circle2.getPerimeter():.2f}\n")

    # Display whether circle1 contains the center of circle2.
    print(f"\ncircle1 contains the center of circle2: "
          f"{circle1.containsPoint(circle2.getXCoordinate(), circle2.getYCoordinate())}")

    # Displays whether circle1 contains circle2.
    print(f"\ncircle1 contains circle2: {circle1.contains(circle2)}")

    # Displays whether circle1 overlaps with circle2.
    print(f"\ncircle1 overlaps with circle2: {circle1.overlaps(circle2)}")

    # Displays whether circle1 is contained in circle2.
    print(f"\ncircle2 contains circle1: {circle2.__contain__(circle1)}")

    # Compares circle1 to circle2.
    print(f"\ncircle1 < circle2: {circle1.__lt__(circle2)}")
    print(f"\ncircle1 <= circle2: {circle1.__le__(circle2)}")
    print(f"\ncircle1 > circle2: {circle1.__gt__(circle2)}")
    print(f"\ncircle1 >= circle2: {circle1.__ge__(circle2)}")
    print(f"\ncircle1 != circle2: {circle1.__ne__(circle2)}")
    print(f"\ncircle1 == circle2: {circle1.__eq__(circle2)}")


if __name__ == "__main__":
    main()
