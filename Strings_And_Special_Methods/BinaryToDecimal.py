"""
    This is a program that uses a function with the header;
                def binaryToDecimal(binaryString):
    to convert a binary string to a decimal number.
"""


def checkBinaryString(binaryValue):
    """
    Checks if the binary value is valid.

    :param binaryValue: The binary value to be checked.

    :return: (bool) True if the binary value is valid, otherwise False.
    """
    for character in binaryValue:
        if character not in "01":
            return False
    return True


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

    # Checks if the binary string entered by the user is valid.
    if not checkBinaryString(binaryString):
        print("\nInvalid binary string!")
        exit(1)

    # Converts the binary string to decimal and displays the result.
    print(f"\nThe decimal equivalent of '{binaryString}' is: {binaryToDecimal(binaryString)}")


if __name__ == "__main__":
    main()
