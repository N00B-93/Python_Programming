"""
    This is a program that prompts the user to enter a String and then determines the number of uppercase letters in the
    String using a function and a recursive helper function.
"""

numberOfUppercaseLetters: int = 0


def countUppercaseHelper(string: str, high: int):
    """
    Returns the number of uppercase letters in a given String.

    :param string: (str) The string to count the number of uppercase letters.

    :param high: (int) The index of the last element of the String.

    :return: (int) The number of uppercase letters in the given String.
    """
    global numberOfUppercaseLetters

    if high < 0:
        return numberOfUppercaseLetters
    else:
        if 65 <= ord(string[high]) <= 90:
            numberOfUppercaseLetters += 1
    return countUppercaseHelper(string, high - 1)


def countUppercase(string: str):
    """
    Returns the number of uppercase letters in a given String using a recursive helper function.

    :param string: (str) The string to count the number of uppercase letters.

    :return: (int) The number of uppercase letters in the given String.
    """
    return countUppercaseHelper(string, len(string) - 1)


def main() -> None:
    # Prompts the user to enter a String.
    string = input("\nEnter a String: ")

    # Displays the number of uppercase letters in the user input.
    print(f"\nThe number of uppercase letters in '{string}' is: {countUppercase(string)}")


if __name__ == "__main__":
    main()
