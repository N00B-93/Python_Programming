"""
    This is a program that prompts the user to enter a hexadecimal number and then displays the decimal equivalent
    of the number using a recursive function.
"""


def checkHexadecimalNumber(hexString: str) -> bool:
    """
    Checks if the input string is a hexadecimal String.

    :param hexString: (str) The hexadecimal number to be checked.

    :return: (bool) True if the input string is a hexadecimal String, false otherwise.
    """
    for char in hexString:
        if char not in "0123456789ABCDEF":
            return False
    return True


def hexadecimalToDecimalHelper(hexString: str, index: int) -> int:
    """
    Converts the hexadecimal number into it's decimal equivalent.

    :param hexString: (int) The hexadecimal number to be converted.

    :param index: (int) The index or power of each digit in the hexadecimal number.

    :return: (int) The decimal equivalent of the hexadecimal number.
    """
    if index >= 0:
        hexDigit = hexString[index]
        if hexDigit in "ABCDEF":
            return (10 + ord(hexDigit) - 65) * pow(16, index) + hexadecimalToDecimalHelper(hexString, index - 1)
        return int(hexDigit) * pow(16, index) + hexadecimalToDecimalHelper(hexString, index - 1)
    return 0


def hexToDecimal(hexString: str) -> int:
    """
    Converts a hexadecimal string to its decimal equivalent by making a call to a recursive helper function.

    :param hexString: (str) The hexadecimal String to be converted to decimal.

    :return: (int) The decimal equivalent of the hexadecimal string.
    """
    if hexString == '0' or hexString == '1':
        return int(hexString)
    return hexadecimalToDecimalHelper(hexString[::-1], len(hexString) - 1)


def main() -> None:
    while True:
        # Prompts the user to enter a hexadecimal number.
        hexString = input("\nEnter a hexadecimal number: ")

        # Displays an error message if the user input is not a hexadecimal String
        if not checkHexadecimalNumber(hexString):
            print("\nInvalid input, Use numbers containing 1's and 0's only.")
            continue

        # Displays the decimal equivalent of the hexadecimal number entered by the user.
        print(f"\nThe decimal equivalent of {hexString} is: {hexToDecimal(hexString)}")
        break


if __name__ == "__main__":
    main()
