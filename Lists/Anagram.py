from sys import exit


"""
    Two words are anagrams if they contain the same letters.
    This is a program that prompts the user to enter two Strings and determines if they
    are anagrams or not using a function with the header;
                def isAnagram(s1, s2)
"""


def main():
    # Prompts the user to enter two Strings to be compared.
    string1 = input("\nEnter the first string: ")
    string2 = input("\nEnter the second string: ")
    
    # Terminates the program if the Strings have unequal lengths.
    if len(string1) != len(string2):
        print(f"\n{string1} and {string2} are not anagrams.")
        exit(1)

    # Converts the Strings to lists.
    lst1, lst2 = list(string1), list(string2)
    
    # Sorts the two lists.
    lst1.sort()
    lst2.sort()

    # Compares the sorted lists and displays the result.
    if lst1 == lst2:
        print(f"\n{string1} and {string2} are anagrams.")
    else:
        print(f"\n{string1} and {string2} are not anagrams.")


if __name__ == "__main__":
    main()
