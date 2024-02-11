from sys import exit

"""
    An ISBN-10 (International Standard Book Number) Number consists of 10 digits d1d2d3d4d5d6d7d8d9d10.
    The last digit, d10 is a checksum, which is calculated from the other nine digits using the following formula:
                    (d1 * 1 + d2 * 2 + d3 * 3 + d4 * 4 + d5 * 5 + d6 * 6 + d7 * 7 + d8 * 8 + d9 * 9) % 11
    If the checksum is 10, the last digit is denoted as X, according to the ISBN convention.

    This program prompts the user to enter the first 9 digits as a string and displays
    the 10-digit ISBN (including leading zeros).
"""


def main():
    # Reads in the first 9 digits of an ISBN-10 Number.
    isbn10 = input("\nEnter the first 9 digit of an ISBN-10 Number: ")

    # Prints an error message and terminates the program if the length of the number entered is not equal to 9.
    if len(isbn10) != 9:
        print("Invalid input, Enter 9 digits.")
        exit(1)

    total = 0

    # Multiplies each digit by with each value of 1 to 9.
    for i in range(1, 10):
        total += int(isbn10[i - 1]) * i

    # calculates the checkSum.
    checksum = total % 11

    # Displays the result based on the value of the checkSum.
    if checksum == 10:
        print(f"\nThe ISBN-10 number is: {isbn10 + "X"}")
    else:
        print(f"\nThe ISBN-10 number is: {isbn10 + str(checksum)}")


if __name__ == "__main__":
    main()
