"""
    This is a program that prompts the user to enter a positive integer and then displays the Hexadecimal equivalent
    of the number as a String using a recursive function.
"""


def decimalToHexadecimalHelper(number: int, string: str) -> str:
    """
    Recursive helper function that takes a number and a String as input and returns the Hexadecimal representation of
    the number as a String.

    :param number: (int) The decimal number to be converted.

    :param string: (str) A String to hold the Hexadecimal representation of the number.

    :return: (str) The Hexadecimal representation of the decimal number as a String.
    """
    if number > 0:
        remainder = number % 16
        if 10 <= remainder <= 15:
            string += chr(ord('A') + (remainder - 10))
        else:
            string += str(remainder)
        return decimalToHexadecimalHelper(number // 16, string)
    else:
        return string


def decimalToHexadecimal(number: int) -> str:
    """
    Returns the Hexadecimal equivalent of a decimal number by making a call to a recursive helper function.

    :param number: (int) The decimal number to be converted to Hexadecimal.

    :return: (str) The Hexadecimal representation of the decimal number as a String.
    """
    hexString = ""
    if number == 0:
        return "0"
    return decimalToHexadecimalHelper(number, hexString)[::-1]


def main() -> None:
    while True:
        try:
            # Prompts the user to enter a positive integer.
            decimal = int(input("\nEnter a positive integer: "))

            # Continues to loop till the user enters a number greater than or equal to 0.
            while decimal < 0:
                print("\nInvalid input. Try again.")
                decimal = int(input("\nEnter a positive integer: "))
            print(f"\nThe Hexadecimal equivalent of {decimal} is: {decimalToHexadecimal(decimal)}")
            break
        except ValueError:
            print("\nInvalid input. Try again.")


if __name__ == "__main__":
    main()
