"""
    This is a program that prompts the user to enter a String and then displays the String in reverse using
    a recursive function and a recursive helper function.
"""


def reverseDisplayHelper(string: str, high: int) -> None:
    """
    Displays a String in reverse using recursively by taking the String and the index of the last character of the
    String from another recursive function.

    :param string: (str) The string to be displayed in reverse.

    :param high: (int) The index of the last character in the String to be displayed.

    :return: None
    """
    if high < 0:
        return
    else:
        print(f"{string[high]}", end="")
    reverseDisplayHelper(string, high - 1)


def reverseDisplay(string: str) -> None:
    """
    Displays a String in reverse with the help of a recursive helper function.

    :param string: (str) The string to be displayed in reverse.

    :return: None.
    """
    reverseDisplayHelper(string, len(string) - 1)


def main() -> None:
    # Prompts the user to enter a String.
    string = input("\nEnter a string to be displayed in reverse: ")

    # Displays the String in reverse.
    print(f"\nThe reversed of '{string}' is: ", end="")
    reverseDisplay(string)
    print()


if __name__ == "__main__":
    main()
