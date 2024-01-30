class Rectangle:
    """
    A class representing a Rectangle.

    Attributes:

        width (float): The width of the rectangle.

        height (float): The height of the rectangle.
    """
    def __init__(self, height=1.0, width=2.0):
        """
        Initializes a rectangle with the given height and width.

        :param height: (float) The height of the rectangle.

        :param width: (float) The width of the rectangle.
        """
        self.height = height
        self.width = width

    def getArea(self):
        """
        Returns the area of the rectangle.

        :return: (float) The area of the rectangle.
        """
        return self.height * self.width

    def getPerimeter(self):
        """
        Returns the perimeter of the rectangle.

        :return: (float) The perimeter of the rectangle.
        """
        return 2 * (self.height + self.width)


def main():
    # Creates two Rectangle Objects.
    rectangle1 = Rectangle(4, 40)
    rectangle2 = Rectangle(3.5, 35.7)

    # Displays the properties of rectangle1.
    print("\nRectangle1: ")
    print("Height: ", rectangle1.height, "\nWidth: ", rectangle1.width, "\nArea: ", format(rectangle1.getArea(), ".2f"),
          "\nPerimeter: ", format(rectangle1.getPerimeter(), ".2f"), sep="")

    # Displays the properties of rectangle2.
    print("\nRectangle2:")
    print("Height: ", rectangle2.height, "\nWidth: ", rectangle2.width, "\nArea: ", format(rectangle2.getArea(), ".2f"),
          "\nPerimeter: ", format(rectangle2.getPerimeter(), ".2f"), sep="")


if __name__ == "__main__":
    main()
