from math import sqrt


class Complex1:
    """
    A class representing complex numbers.

    Attributes:
        realPart: (float) The real part of the complex number.

        imaginaryPart: (float) The imaginary part of the complex number.
    """
    def __init__(self, realPart=0.0, imaginaryPart=0.0):
        self.realPart = realPart
        self.imaginaryPart = imaginaryPart

    def getRealPart(self) -> float:
        """
        This returns the real part of a Complex1 number.

        Returns: (float) The real part of a complex number.
        """
        return self.realPart

    def getImaginaryPart(self) -> float:
        """
        This returns the imaginary part of a Complex1 number.

        Returns: (float) The imaginary part of a Complex1 number.
        """
        return self.imaginaryPart

    def __str__(self) -> str:
        """
        This returns a String representation of a Complex1 number.

        Returns: (str) The String representation of a Complex1 number.
        """
        if self.realPart == 0:
            return f"{self.getImaginaryPart()}i"
        elif self.imaginaryPart == 0:
            return f"{self.realPart}"
        return f"{self.getRealPart()} + {self.getImaginaryPart()}i"

    def __add__(self, other):
        """
        Determines the sum of two Complex1 numbers.

        Args:
            other: (Complex1) The Complex1 number to be added to the current instance.

        Returns: (Complex1) The sum of two Complex1 numbers.
        """
        result = Complex1()

        result.realPart = self.realPart + other.realPart
        result.imaginaryPart = self.imaginaryPart + other.imaginaryPart

        return result

    def __sub__(self, other):
        """
        Determines the difference of two Complex1 numbers.

        Args:
            other: (Complex1) The Complex1 number to be subtracted from the current instance.

        Returns: (Complex1) The difference of two Complex1 numbers.
        """
        result = Complex1()

        result.realPart = self.realPart - other.realPart
        result.imaginaryPart = self.imaginaryPart - other.imaginaryPart

        return result

    def __abs__(self) -> float:
        """
        This determines the absolute value of a Complex1 number.

        Returns: (float) The absolute value of a Complex1 number.
        """
        return sqrt(pow(self.realPart, 2) + pow(self.imaginaryPart, 2))

    def __mul__(self, other):
        """
        This determines the product of two Complex1 numbers.

        Args:
            other: (Complex1) The second Complex1 number to be multiplied with the current instance.

        Returns: (float) The product of two Complex1 numbers.
        """
        result = Complex1()

        result.realPart = self.realPart * other.realPart - self.imaginaryPart * other.imaginaryPart
        result.imaginaryPart = self.realPart * other.imaginaryPart + self.imaginaryPart * other.realPart

        return result

    def __truediv__(self, other):
        """
        This determines the true division of two Complex1 numbers.

        Args:
            other: (Complex1) The second Complex1 number.

        Returns: (Complex1) The quotient of the two Complex1 numbers.
        """
        conjugateDenominator = Complex1(other.realPart, -other.imaginaryPart)
        numerator = self * conjugateDenominator
        denominator = other * conjugateDenominator

        return Complex1(numerator.realPart / denominator.realPart, numerator.imaginaryPart / denominator.realPart)
