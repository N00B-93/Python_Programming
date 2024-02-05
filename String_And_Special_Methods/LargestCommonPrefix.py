"""
    This is a program that uses a function with the header;
                def prefix(s1, s2)
    to find the largest common prefix of two Strings entered by the user.
"""


def prefix(s1, s2):
    """
    Returns the largest common prefix of two Strings.

    :param s1: (str) The first String.

    :param s2: (str) The second String.

    :return: (str) The largest common prefix of two Strings.
    """
    counter = 0

    while counter < len(s1) and counter < len(s2) and s1[counter] == s2[counter]:
        counter += 1
    return s1[:counter]


def main():
    # Reads in two Strings.
    string1 = input("\nEnter the first string: ")
    string2 = input("\nEnter the second string: ")

    # Display their largest common prefix.
    print(f"\nThe largest common prefix is: {prefix(string1, string2)}")


if __name__ == "__main__":
    main()
