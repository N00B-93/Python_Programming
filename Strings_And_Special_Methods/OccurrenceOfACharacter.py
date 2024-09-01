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

    # Displays an error message and terminates the program if the user enters an empty String.
    if string == '':
        print("\nError: Use non empty strings only, Try again.")
        exit(1)

    char = input("\nEnter a character whose occurrence is to be counted: ")

    # Displays an error message and terminates the program if the user enters an empty character.
    if char == '':
        print("\nError: Enter a valid character, Try again.")
        exit(2)

    # Determines the number of occurrence of the character in the String.
    occurrences = count(string, char)

    # Displays the result.
    print(f"\nThe occurrences of '{char}' in {string} is: '{occurrences}'.")


if __name__ == "__main__":
    main()
