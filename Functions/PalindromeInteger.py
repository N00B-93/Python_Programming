"""
    This is a program that uses the functions;
            def reverse(number)

            def isPalindrome(number)
    to determine whether a number is palindrome or not.
"""


def reverse(number):
    """
    This function returns the reverse of an integer.
    :param number: (int) The number to be reversed.
    :return: (int) The reversed number.
    """

    reversedNumber = 0

    while number != 0:
        remainder = number % 10

        reversedNumber = reversedNumber * 10 + remainder

        number = number // 10

    return reversedNumber


def isPalindrome(number):
    """
    Checks if a number is a palindrome or not.
    :param number: (int) The number to be checked.
    :return: (boolean) True if the number is palindrome otherwise False
    """

    if number == reverse(number):
        return True
    return False


def main():
    # Reads in a number to be checked.
    number = int(input("\nEnter a number: "))

    # Displays whether the number is a palindrome or not.
    if isPalindrome(number):
        print(f"\n{number} is a palindrome.")
    else:
        print(f"\n{number} is not a palindrome.")


if __name__ == "__main__":
    main()
