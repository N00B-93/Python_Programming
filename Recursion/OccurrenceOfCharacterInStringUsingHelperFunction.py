"""
    This is a program that prompts the user to enter a Character and a String and then determines the number of
    occurrence of the character in the String using a function and a recursive helper function.
"""

# Global variable to hold the number of occurrence of a character.
counter = 0


def countHelper(string: str, character: str, high: int) -> int:
    """
    Returns the number of occurrences of the character in the String using recursion.

    :param string: (str) The string to be processed.

    :param character: (str) The character whose occurrence is to be determined.

    :param high: (int) The index of the last character in the String.

    :return: (int) The number of occurrences of the character in the String.
    """
    global counter

    if high < 0:
        return counter
    elif character == string[high]:
        counter += 1
    return countHelper(string, character, high - 1)


def count(string: str, character: str) -> int:
    """
    Returns the number of occurrences of the character in the String using a recursive helper function.

    :param string: (str) The string to be processed.

    :param character: (str) The character whose occurrences will be determined.

    :return: (int) The number of occurrences of the character in the String.
    """
    return countHelper(string, character, len(string) - 1)


def main() -> None:
    # Prompts the user to enter a String.
    string = input("\nEnter a String: ")

    # Prompts the user to enter a character whose number of occurrence is to be counted.
    character = input("\nEnter a Character whose occurrence is to be counted: ")

    # Displays the result.
    print(f"\nThe number of occurrence of '{character}' in '{string}' is: {count(string, character)}")


if __name__ == "__main__":
    main()
