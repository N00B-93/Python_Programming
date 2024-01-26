"""
    This is a program that prints the characters from 1 to Z taking 10 characters per line
    by using the function with the header;
                def printChars(ch1, ch2, numberPerLine)
    that prints the characters from ch1 and ch2 with the specified numbers per line
"""


def printChars(ch1, ch2, numberPerLine):
    """
    Prints the characters from ch1 and ch2 with the specified numbers per line

    :param ch1: (int) The first character to be printed.

    :param ch2: (int) The last character to be printed.

    :param numberPerLine: (int) The number of characters per line.

    :return: None
    """

    for i in range(ch1, (ch2 + 1)):
        print(f"{chr(i)} ", end="")
        numberPerLine += 1
        if numberPerLine % 10 == 0:
            print()
    return


def main():
    print("\nThe characters from 1 to Z are: ")

    printChars(49, 90, 10)


if __name__ == "__main__":
    main()
