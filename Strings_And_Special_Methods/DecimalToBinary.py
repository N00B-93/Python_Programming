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
    decimalNumber = input("\nEnter a decimal Integer: ")

    # if-elif block that validates user's input.
    if decimalNumber == '':
        print("\nError: Use integers only, Try again.")
        exit(1)
    elif int(decimalNumber) < 0:
        print("\nError: Use positive integers only, Try again.")
        exit(2)

    # Displays the result.
    print(f"\nThe binary equivalent of {decimalNumber} is: {decimalToBinary(int(decimalNumber))}")


if __name__ == "__main__":
    main()
