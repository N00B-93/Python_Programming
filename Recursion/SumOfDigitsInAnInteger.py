"""
    This is a program that prompts the user to enter an integer and the sums up the digits of the
    integer using recursion.
"""


def recursiveSumOfDigits(number: int):
    """
    This returns the sum of digits in an integer using recursion.
    :param number: (int) The number whose sum of digits is to be found.
    :return: (int) The sum of digits in an integer.
    """
    if number == 0:
        return number
    remainder = number % 10
    return remainder + recursiveSumOfDigits(number // 10)


def main() -> None:
    while True:
        try:
            # Prompts the user to enter an integer.
            number: int = int(input("\nEnter a number whose digits is to be summed: "))

            # Display the sum of digits in the number.
            print(f"\nThe sum of digits in {number} is: ", end="")
            print(recursiveSumOfDigits(number))
            break
        except ValueError:
            print("\nInvalid input. Please try again.")


if __name__ == "__main__":
    main()
