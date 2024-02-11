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

    subStringCheck = True

    for i in range(len(s1)):
        # Initializes a counter variable to the current value of i.
        k = i
        for j in range(len(s2)):
            # Compares the current character in s1 to the current character in s2.
            if s1[k] == s2[j]:
                k += 1
                continue
            # Breaks out of the inner loop if the characters don't match.
            else:
                subStringCheck = False
                break
        # Increments counter if the current portion of the string that is checked is a substring.
        if subStringCheck:
            counter += 1
        # Resets the subStringCheck variable back to True.
        subStringCheck = True

    return counter


def main():
    # Reads in two Strings.
    s1 = input("\nEnter the first string: ")
    s2 = input("\nEnter the second string: ")

    # Displays the result.
    print(f"\nThe number of occurrences of '{s2}' in '{s1}' is: {count(s1, s2)}")


if __name__ == "__main__":
    main()
