"""
    This is a program that prompts the user to enter two Strings and then displays;
        • the characters that occur in both strings.
        • the characters that occur in one string but not the other.
        • the letters that don’t occur in either string.
"""


def main() -> None:
    # Reads in the first String.
    string1: str = input("\nEnter the first String: ")

    # Reads in the second String.
    string2: str = input("\nEnter the second String: ")
    
    # Construct a set of characters from the first String.
    setOfCharacters1: set = set(string1.lower())

    # Construct a set of characters from the first String.
    setOfCharacters2: set = set(string2.lower())

    # Displays the characters that occurs in both Strings.
    if len(setOfCharacters1.intersection(setOfCharacters2)) != 0:
        print(f"\nThe characters common to '{string1}' and '{string2}' is: "
              f"{setOfCharacters1.intersection(setOfCharacters2)}")
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

    # Set to hold all the letters common to both Strings.
    unionOfLetters: set = setOfCharacters1.union(setOfCharacters2)

    # Creates a set of alphabets in lower case from a - z.
    alphabets = set()
    for i in range(97, 123):
        alphabets.add(chr(i))

    # Displays the letters that don't occur in either of the Strings.
    print("\nThe letters that don't occur in either String are: ", end="")
    for letter in alphabets:
        if letter not in unionOfLetters:
            print(f"{letter} ", end="")
    print()


if __name__ == "__main__":
    main()
