"""
    This is a program that prompts the userv to enter a String and then displays the String
    in reverse using recursion.
"""


def reverseDisplay(string: str) -> None:
    """
    Displays a String in reverse using recursion.

    :param string: (str) The string to be displayed in reverse.

    :return: None.
    """
    if len(string) == 1:
        print(string, end="")
    else:
        print(f"{string[len(string) - 1]}", end="")
        reverseDisplay(string[0:len(string) - 1])


def main() -> None:
    # Prompts the user to enter a String to be reversed.
    string = input("\nEnter a string to be displayed in reverse: ")

    # Displays the original String.
    print(f"\nOriginal String: {string}")

    # Displays the reversed String.
    print("\nReversed String: ", end="")
    reverseDisplay(string)
    print()


if __name__ == "__main__":
    main()
