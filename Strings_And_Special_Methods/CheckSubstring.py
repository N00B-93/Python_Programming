"""
    This is a program that prompts the user to enter two strings and then checks
    whether the first string is a substring of the second string
"""


def isSubString(mainString: str, otherString: str) -> bool:
    """
    This determines whether a String is a sub String of another.

    Args:
        mainString: (str) The first String.
        otherString: (str) The String to be searched for in the main String

    Returns: True if the other string is a sub String of the main String, else False.

    """
    for i in range(len(mainString) - (len(otherString) - 1)):
        if mainString[i] == otherString[0]:
            k, j = i, 0
            # Iterate over each character of otherString.
            for j in range(len(otherString)):
                # Check if characters match
                if mainString[k] != otherString[j]:
                    break
                k = k + 1
            # If all characters match, return True.
            if j == len(otherString) - 1:
                return True
    return False


def main() -> None:
    while True:
        # Prompts the user to enter a String.
        mainString: str = input("\nEnter a String: ").strip()

        # Prompts the user to enter the sub String to be searched for.
        subString: str = input("\nEnter the sub String to be searched for: ").strip()

        if mainString != "" and subString != "":
            break
        else:
            print("\nError: Use non empty Strings only, Try again.")

    # Displays the result.
    print(f"\nIs '{subString}' a substring of '{mainString}'? {isSubString(mainString, subString)}")


if __name__ == "__main__":
    main()
