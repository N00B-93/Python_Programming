from BinaryToDecimal import binaryToDecimal
from sys import exit

"""
    This is a program that uses a  function with the header;
                binaryToHex(binaryValue):
to convert a binary value into a hexadecimal.
"""


def binaryToHex(binaryValue):
    # Converts the binary string to decimal.
    decimal = binaryToDecimal(binaryValue)

    hexNumber = ""
    while decimal > 0:
        # Extracts the last digit of decimal number.
        remainder = decimal % 16
        # Adds the remainder to the hexNumber.
        if 10 <= remainder <= 15:
            hexNumber += chr(remainder - 10 + ord("A"))
        else:
            hexNumber += str(remainder)
        # Peels of the last digit of decimal number.
        decimal //= 16
    # Returns the reverse of hexNumber.
    return hexNumber[::-1]


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


def main():
    binaryNumber = input("\nEnter the binary string: ")

    # Checks if the binary string entered by the user is valid.
    if not checkBinaryString(binaryNumber):
        print("\nInvalid binary string!")
        exit(1)

    # Displays the result.
    print(f"\nThe Hexadecimal equivalent of '{binaryNumber}' is: {binaryToHex(binaryNumber)}")


if __name__ == "__main__":
    main()
