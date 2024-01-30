from math import sqrt


class QuadraticEquation:
    """
    A class representing an Equation.

    Attributes:

        a (float): The coefficient of x^2

        b (float): The coefficient of x.

        c (float): The constant.
    """
    def __init__(self, a, b, c):
        """
        Initializes a QuadraticEquation Object with a given set of values.

        :param a: The coefficient of x^2

        :param b: The coefficient of x.

        :param c: The constant.
        """
        self.__a = a
        self.__b = b
        self.__c = c

    def getA(self):
        """
        Returns the value of the coefficient a.

        :return: (float): The value of the coefficient a.
        """
        return self.__a

    def getB(self):
        """
        Returns the value of the coefficient b.

        :return: (float): The value of the coefficient b.
        """
        return self.__b

    def getC(self):
        """
        Returns the value of the coefficient c.

        :return: (float): The value of the coefficient c.
        """
        return self.__c

    def getDiscriminant(self):
        """
        Returns the value of the discriminant of the equation.

        :return: (float): The value of the discriminant of the equation.
        """
        return self.__b ** 2 - 4 * self.__a * self.__c

    def getRoot1(self):
        """
        Returns the first root of a quadratic equation.

        :return: (float) The first root of a quadratic equation.
        """
        return (-self.__b + sqrt(self.getDiscriminant())) / (2 * self.__a)

    def getRoot2(self):
        """
        Returns the second root of a quadratic equation.

        :return: (float) The second root of a quadratic equation.
        """
        return (-self.__b - sqrt(self.getDiscriminant())) / (2 * self.__a)


def main():
    # Reads in coefficient of an equation.
    a, b, c = eval(input("\nEnter the coefficients of ax^2 + bx + c separated by comma: "))

    # Creates an Equation Object.
    equation1 = QuadraticEquation(a, b, c)

    # Displays the roots of the equation.
    if equation1.getDiscriminant() > 0:
        print(f"\nThe roots are: {equation1.getRoot1()}, {equation1.getRoot2()}")
    elif equation1.getDiscriminant() == 0:
        print(f"\nThe root is: {equation1.getRoot1()}")
    else:
        print("\nThe equation has no root!")


if __name__ == "__main__":
    main()
