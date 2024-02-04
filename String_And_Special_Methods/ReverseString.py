"""
    This is a program that uses a function with the header;
                def reverse(s):
    to reverse a string entered by the user.
"""


def reverse(s):
    """
    Reverses a string.

    :param s: (str) The string to be reversed.

    :return: (str) The reversed string.
    """
    return s[::-1]


def main():
    # Reads in a string to be reversed.
    string = input("\nEnter a string to be reversed: ")

    # Displays the result.
    print(f"\nThe reversed string is: {reverse(string)}")


if __name__ == "__main__":
    main()
