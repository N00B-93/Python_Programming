"""
    This is a program that prompts the user to enter a String and then capitalizes the first character
    of each word in the String.
"""


def capitalize(string: str) -> str:
    """
    This returns a String with the first letter of each word in the String capitalized.

    :param string: (str) The String to be processed.

    :return: (str) A String with first letter of each word in the String capitalized.
    """
    capitalizedString: str = string[0].upper()

    for i in range(1, len(string)):
        if string[i - 1] == " ":
            capitalizedString += string[i].upper()
        else:
            capitalizedString += string[i]
    return capitalizedString


def main() -> None:
    # Prompts the user to enter a String to be capitalized.
    string: str = input("\nEnter a String to be capitalized: ")
    
    # Continues to loop till the user enters a String whose length is greater than 1.
    while len(string) < 1:
        print("\nInvalid input, Use a String with length greater than 1.")
        string = input("\nEnter a String to be capitalized: ")

    # Displays the original String and the Capitalized String.
    print(f"\nOriginal String: {string}")
    print(f"\nCapitalized String: {capitalize(string)}")


if __name__ == "__main__":
    main()
