"""
    This is a program that prompts the user to enter a binary number and then displays the decimal equivalent
    of the number using a recursive function.
"""


def checkBinaryNumber(binString: str) -> bool:
    """
    Checks if the input string is a binary String, i.e., if the input string is made up of '0' and '1'.

    :param binString: (str) The binary number to be checked.

    :return: (bool) True if the input string is a binary String, false otherwise.
    """
    for char in binString:
        if char not in "01":
            return False
    return True


def binaryToDecimalHelper(binNumber: int, index: int) -> int:
    """
    Converts the binary number into it's decimal equivalent.

    :param binNumber: (int) The binary number to be converted.

    :param index: (int) The index or power of each digit in the binary number.

    :return: (int) The decimal equivalent of the binary number.
    """
    if binNumber > 0:
        remainder = binNumber % 10
        return remainder * pow(2, index) + binaryToDecimalHelper(binNumber // 10, index + 1)
    else:
        return binNumber


def binToDecimal(binString: str) -> int:
    """
    Converts a binary string to its decimal equivalent by making a call to a recursive helper function.

    :param binString: (str) The binary String to be converted to decimal.

    :return: (int) The decimal equivalent of the binary string.
    """
    if binString == '0' or binString == '1':
        return int(binString)
    return binaryToDecimalHelper(int(binString), 0)


def main() -> None:
    while True:
        # Prompts the user to enter a binary number.
        binString = input("\nEnter a binary number: ")

        # Displays an error message if the user input is not a binary String
        if not checkBinaryNumber(binString):
            print("\nInvalid input, Use numbers containing 1's and 0's only.")
            continue

        # Displays the decimal equivalent of the binary number entered by the user.
        print(f"\nThe decimal equivalent of {binString} is: {binToDecimal(binString)}")
        break


if __name__ == "__main__":
    main()
