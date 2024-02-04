"""
    This is a program that uses a function with the header;
                def count(s, ch):
    to determine the occurrence of a character in string.
"""


def count(string, ch):
    """
    Determines the occurrence of a character in string.

    :param string: (string) The string to be processed.

    :param ch: (char) The character to be counted.

    :return: (int) The number of occurrences of the character in string.
    """
    occurrences = 0

    for character in string:
        if character == ch:
            occurrences += 1
    return occurrences


def main():
    # Reads in a String and a Character whose occurrence in the string is to be counted.
    string = input("\nEnter a string: ")
    ch = input("\nEnter a character whose occurrence is to be counted: ")

    occurrences = count(string, ch)

    print(f"\nThe occurrences of '{ch}' in {string} is: '{occurrences}'.")


if __name__ == "__main__":
    main()
