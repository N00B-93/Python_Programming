"""
    This is a program that prompts the user to enter two non-negative integers greater than 0 and determines their
    greatest common divisor(GCD) using recursion.
"""


def greatestCommonDivisor(number1: int, number2: int):
    """
    This returns the greatest common divisor of two positive integers.
    :param number1: (int) The first integer.
    :param number2: (int) The second integer.
    :return: (int) The greatest common divisor(GCD) of two positive integers.
    """
    if number1 % number2 == 0:
        return number2
    return greatestCommonDivisor(number1, number1 % number2)


def main() -> None:
    while True:
        try:
            # Prompts the user to enter the first number.
            number1: int = int(input("\nEnter the first number: "))

            # Prompts the user to enter the second number.
            number2: int = int(input("\nEnter the second number: "))

            # Displays the Greatest Common Divisor(GCD) of the two numbers.
            if number2 > number1:
                print(f"\nThe greatest common divisor of {number1} and {number2} is: "
                      f"{greatestCommonDivisor(number2, number1)}")
                break
            else:
                print(f"\nThe greatest common divisor of {number1} and {number2} is: "
                      f"{greatestCommonDivisor(number1, number2)}")
                break
        except ValueError:
            print("\nInvalid input. Try again.")


if __name__ == "__main__":
    main()
