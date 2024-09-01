"""
    This is a program that prompts the user to enter two strings and then uses a function with the header;
                def count(s1, s2):
    to count the occurrence of a string s2 in another string s1.
"""


def count(s1, s2):
    """
    To count the occurrence of a string s2 in another string s1.

    :param s1: (str) The first string.

    :param s2: (str) The second string whose occurrence is to be counted.

    :return: (int) The number of occurrences of the second string.
    """
    counter = 0

    for k in range(len(s1) - len(s2) + 1):
        if s1[k] == s2[0] and s1[k:k + len(s2)] == s2:
            counter += 1
    return counter


def main():
    while True:
        # Reads in two Strings.
        s1 = input("\nEnter the first string: ").strip()
        s2 = input("\nEnter the second string: ").strip()

        if s1 != "" and s2 != "":
            break
        else:
            print("\nError: Use non empty Strings only, Try again.")

    # Displays the result.
    if len(s1) >= len(s2):
        print(f"\nThe number of occurrences of '{s2}' in '{s1}' is: {count(s1, s2)}")
    elif len(s2) > len(s1):
        print(f"\nThe number of occurrences of '{s1}' in '{s2}' is: {count(s2, s1)}")


if __name__ == "__main__":
    main()
