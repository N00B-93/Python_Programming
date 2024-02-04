"""
    This is a program that uses a function with the header;
                def binaryToDecimal(binaryString):
    to convert a binary string to a decimal number.
"""


def binaryToDecimal(binaryString):
    """
    Convert a binary string to a decimal number.

    :param binaryString: (str) The binary string to be converted.

    :return: (int) The decimal equivalent of the binary string.
    """
    index = len(binaryString) - 1

    decimal = 0
    positionIndex = 0

    while index >= 0:
        decimal += int(binaryString[positionIndex]) * (2 ** index)
        index -= 1
        positionIndex += 1
    return decimal


def main():
    # Reads in a binary string.
    binaryString = input("\nEnter a binary string: ")

    # Converts the binary string to decimal and displays the result.
    print(f"\nThe decimal equivalent of '{binaryString}' is: {binaryToDecimal(binaryString)}")


if __name__ == "__main__":
    main()
