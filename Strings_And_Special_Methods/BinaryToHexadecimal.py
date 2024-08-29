from BinaryToDecimal import binaryToDecimal, checkBinaryString
from sys import exit

"""
    This is a program that uses a  function with the header;
                binaryToHex(binaryValue):
to convert a binary value into a hexadecimal.
"""


def binaryToHex(binaryValue):
    """
    Converts a binary String into an hexadecimal String.

    Parameter:
        binaryValue (str): A String representing a binary number.
    
    Returns:
        (str): The hexadecimal equivalent of a binary number.
    """
    # Converts the binary string to decimal.
    decimal = binaryToDecimal(binaryValue)

    hexNumber = []

    while decimal > 0:
        # Extracts the last digit of decimal number.
        remainder = decimal % 16
        # Adds the remainder to the hexNumber.
        if 10 <= remainder <= 15:
            hexNumber.append(chr(remainder - 10 + ord("A")))
        else:
            hexNumber.append( str(remainder))
        # Peels of the last digit of decimal number.
        decimal //= 16

    hexString = ''.join(hexNumber)

    # Returns the reverse of hexNumber.
    return hexString[::-1]


def main():
    binaryNumber = input("\nEnter the binary string: ")

    # Checks if the binary string entered by the user is valid.
    if not checkBinaryString(binaryNumber):
        print("\nInvalid binary string!")
        exit(1)
    elif binaryNumber == '':
        print("\nError: Use non empty Strings only, Try again.")
        exit(2)

    # Displays the result.
    print(f"\nThe Hexadecimal equivalent of '{binaryNumber}' is: {binaryToHex(binaryNumber)}")


if __name__ == "__main__":
    main()
