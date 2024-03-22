"""
    This is a program that prompts the user to enter a positive integer and then displays the binary equivalent
    of the number as a String using a recursive function.
"""


def decimalToBinaryHelper(number: int, string: str) -> str:
    """
    Recursive helper function that takes a number and a String as input and returns the binary representation of
    the number as a String.

    :param number: (int) The decimal number to be converted.

    :param string: (str) A String to hold the binary representation of the number.

    :return: (str) The binary representation of the decimal number as a String.
    """
    if number > 0:
        remainder = number % 2
        string += str(remainder)
        return decimalToBinaryHelper(number // 2, string)
    else:
        return string


def decimalToBinary(number: int) -> str:
    """
    Returns the binary equivalent of a decimal number by making a call to a recursive helper function.

    :param number: (int) The decimal number to be converted to binary.

    :return: (str) The binary representation of the decimal number as a String.
    """
    binString = ""
    if number == 0:
        return "0"
    return decimalToBinaryHelper(number, binString)[::-1]


def main() -> None:
    while True:
        try:
            # Prompts the user to enter a positive integer.
            decimal = int(input("\nEnter a positive integer: "))

            # Continues to loop till the user enters a number greater than or equal to 0.
            while decimal < 0:
                print("\nInvalid input. Try again.")
                decimal = int(input("\nEnter a positive integer: "))
            print(f"\nThe binary equivalent of {decimal} is: {decimalToBinary(decimal)}")
            break
        except ValueError:
            print("\nInvalid input. Try again.")


if __name__ == "__main__":
    main()
