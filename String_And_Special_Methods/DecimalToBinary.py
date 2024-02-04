"""
    This is a program that uses a function with the header;
                def decimalToBinary(value):
    to convert a decimal number to its binary equivalent.
"""


def decimalToBinary(value):
    """
    Convert a decimal number to its binary equivalent.

    :param value: (int) The decimal to be converted.

    :return: (str) The binary equivalent of the decimal value.
    """
    binaryNumber = ""

    while value > 0:
        remainder = value % 2
        binaryNumber += str(remainder)
        value = value // 2

    # Returns the reverse of the binary number.
    return binaryNumber[::-1]


def main():
    # Reads in a decimal Integer to be converted to binary.
    decimalNumber = int(input("\nEnter a decimal Integer: "))

    # Displays the result.
    print(f"\nThe binary equivalent of {decimalNumber} is: {decimalToBinary(decimalNumber)}")


if __name__ == "__main__":
    main()
