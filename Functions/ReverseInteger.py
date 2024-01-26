"""
    This is a program that uses a function with header;
            def reverse(number)
    to reverse an integer entered by the user.
"""


def reverse(number):
    """
    This function returns the reverse of a positive integer.
    :param number: (int) The number to be reversed.
    :return: (int) The reversed number.
    """

    reversedNumber = 0

    while number != 0:
        remainder = number % 10

        reversedNumber = reversedNumber * 10 + remainder

        number = number // 10

    return reversedNumber


def main():
    number = int(input("\nEnter a positive integer to be reversed: "))

    print(f"\nThe reverse of {number} is: {reverse(number)}")


if __name__ == "__main__":
    main()
