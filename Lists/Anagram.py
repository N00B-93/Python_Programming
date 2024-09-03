from sys import exit


"""
    Two words are anagrams if they contain the same letters.
    This is a program that prompts the user to enter two Strings and determines if they
    are anagrams or not using a function with the header;
                def isAnagram(s1, s2)
"""

def isAnagram(s1, s2):
    """
    Determines whether two Strings are anagrams.

    Parameters:
        s1 (str): The first String.

        s2 (str): The second String.

    Returns:
        bool: True if the Strings are anagrams, else False.
    """
    if len(s1) != len(s2):
        return False

    lst1, lst2 = list(s1.lower()), list(s2.lower())

    lst1.sort()
    lst2.sort()

    return lst1 == lst2


def main():
    # Prompts the user to enter two Strings to be compared.
    string1 = input("\nEnter the first string: ").strip()
    string2 = input("\nEnter the second string: ").strip()
    # Validate user input.
    if not string1 or not string2:
        print("\nError: Both Strings must be non-empty Strings only, Try again")
        exit(1)
    elif not string1.isalpha() or not string2.isalpha():
        print("\nError: Both Strings must be alphabetic, Try again")
        exit(2)

    # Displays the result.
    if isAnagram(string1, string2):
        print(f"\n{string1} and {string2} are anagrams.")
    else:
        print(f"\n{string1} and {string2} are not anagrams.")


if __name__ == "__main__":
    main()
