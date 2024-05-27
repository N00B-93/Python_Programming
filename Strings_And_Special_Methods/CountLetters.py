"""
    This is a program that uses a function with the header;
                def countLetters(s):
    to count the number of letters in a string.
"""


def countLetters(string):
    """
    Counts the number of letters in a string.

    :param string: (str) The string to be processed.

    :return: (int) The number of letters in the string.
    """
    letterCounter = 0

    for character in string:
        # Increments letterCounter if character is a letter.
        if character.isalpha():
            letterCounter += 1
    return letterCounter


def main():
    # Prompts the user to enter a string.
    string = input("\nEnter a string: ")
    
    # Displays an error message and continue to prompt the user to enter a non-empty string.
    while string == '':
        print("\nError: Use non empty strings containing letters only, Try again.")
        string = input("\nEnter a string: ")

    print(f"\nNumber of letters in '{string}' is: {countLetters(string)}")


if __name__ == "__main__":
    main()
