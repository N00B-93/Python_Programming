"""
    This is a program that uses a function with the header;
            def sumDigits(n):
    to calculate the sum of digits in a number.
"""


def sumDigits(number):
    """
    Function to calculate the sum of digits in a number.
    :param number: (int) The number whose sum of digits is to be calculated.
    :return: (int) The sum of digits in a number
    """

    sumOfDigits = 0

    while number != 0:
        remainder = number % 10

        sumOfDigits += remainder

        number = number // 10

    return sumOfDigits


def main():
    # Reads in a number.
    number = int(input("\nEnter a number: "))

    # Calculates and displays the sum of digits in the number.
    print(f"\nThe sum of digits in {number} is: {sumDigits(number)}")


if __name__ == "__main__":
    main()
