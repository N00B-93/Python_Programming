"""
    This s a program that prompts the user to enter a String and a character and then counts the occurrences
    of that character in the String using recursion.
"""


def countOccurrence(string: str, character: str) -> int:
    """
    This function counts the occurrences of a character in the string using recursion.

    :param string: (str) The string to count occurrences of the character.

    :param character: (str) The character whose occurrence in the String is top be counted.

    :return: (int) The number of occurrences of the character in the string.
    """
    if not string:
        return 0
    else:
        if string[-1] == character:
            return 1 + countOccurrence(string[:-1], character)
        else:
            return countOccurrence(string[:-1], character)


def main() -> None:
    # Prompts the user to enter a String.
    string = input("\nEnter a String: ")

    # Prompts the user to enter the character to be counted in the String.
    character = input("\nEnter a character to count: ")

    # Displays the number of occurrence of the character in the String.
    print(f"\nThe number of occurrence of '{character}' in '{string}' is: {countOccurrence(string, character)}")


if __name__ == "__main__":
    main()
