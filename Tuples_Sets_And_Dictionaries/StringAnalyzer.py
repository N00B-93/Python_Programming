"""
    This is a program that prompts the user to enter two Strings and then displays;
        • the characters that occur in both strings.
        • the characters that occur in one string but not the other.
        • the letters that don't occur in either string.
"""


def main() -> None:
    # Reads in the first String.
    string1: str = input("\nEnter the first String: ")

    # Reads in the second String.
    string2: str = input("\nEnter the second String: ")

    # Validates user input.
    if not string1 or not string2:
        print("\nError: Both Strings entered must be non-empty Strings, Try again with non-empty Strings.")
        exit(1)
    elif not string1.isalpha() or not string2.isalpha():
        print("\nError: Both Strings used must contain only alphabets, Try again with alphabetic Strings.")
        exit(2)
    
    # Construct a set of characters from the first String.
    setOfCharacters1: set = set(string1.lower())

    # Construct a set of characters from the first String.
    setOfCharacters2: set = set(string2.lower())

    # Determines the characters common to the two Strings.
    commonCharacters: set = setOfCharacters1.intersection(setOfCharacters2)

    # Displays the characters that occurs in both Strings.
    if len(commonCharacters) != 0:
        print(f"\nThe characters common to '{string1}' and '{string2}' is: {commonCharacters}")
    else:
        print(f"\n'{string1}' and '{string2}' have no characters in common.")

    # Displays the character that occurs in the first String but not the other.
    if len(setOfCharacters1 - setOfCharacters2) != 0:
        print(f"\nThe letters in '{string1}' that are not in '{string2}' are: "
              f"{setOfCharacters1.difference(setOfCharacters2)}")
    else:
        print(f"\nAll letters present in '{string1}' are also present in '{string2}'")

    # Displays the character that occurs in the second String but not the other.
    if len(setOfCharacters2 - setOfCharacters1) != 0:
        print(f"\nThe letters in '{string2}' that are not in '{string1}' are: "
              f"{setOfCharacters2.difference(setOfCharacters1)}")
    else:
        print(f"\nAll letters present in '{string2}' are also present in '{string1}'")

    # Set to hold all the letters present in both Strings.
    unionOfLetters: set = setOfCharacters1.union(setOfCharacters2)

    # Displays the letters that don't occur in either of the Strings.
    print("\nThe letters that don't occur in either String are: ", end="")
    for letter in range(97, 123):
        if chr(letter) not in unionOfLetters:
            print(f"{chr(letter)} ", end="")
    print()


if __name__ == "__main__":
    main()
