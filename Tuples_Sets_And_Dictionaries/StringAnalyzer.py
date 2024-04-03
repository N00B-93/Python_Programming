"""
    This is a program that prompts the user to enter two Strings and then displays;
        • the characters that occur in both strings.
        • the characters that occur in one string but not the other.
        • the letters that don’t occur in either string.
"""


def main() -> None:
    # Reads in the first String.
    string1 = input("\nEnter the first String: ")

    # Reads in the second String.
    string2 = input("\nEnter the second String: ")
    
    # Construct a set of characters from the first String.
    setOfCharacters1 = set(string1)

    # Construct a set of characters from the first String.
    setOfCharacters2 = set(string2)

    # Displays the characters that occurs in both Strings.
    if len(setOfCharacters1.intersection(setOfCharacters2)) != 0:
        print(f"\nThe characters common to '{string1}' and '{string2}' is: {setOfCharacters1.intersection(setOfCharacters2)}")

    # Displays the character that occurs in the first String but not the other.
    if len(setOfCharacters1 - setOfCharacters2) != 0:
        print(f"\nThe letters in '{string1}' that are not in '{string2}' are: {setOfCharacters1.difference(setOfCharacters2)}")


if __name__ == "__main__":
    main()

