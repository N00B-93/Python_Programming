from sys import exit


"""
    ISBN-13 is a new standard for identifying books. It uses 13 digits: d1d2d3d4d5d6d7d8d9d10d11d12d13.
    The last digit, d13 is a checksum, which is calculated from the other digits using the following formula:
                10 - (d1 + 3d2 + d3 + 3d4 + d5 + 3d6 + d7 + 3d8 + d9 + 3d10 + d11 + 3d12) % 10
    If the checksum is 10, it is replaced with 0.
        This program prompts the user to enter the first 12 digits as a string and displays
    the 13-digit ISBN (including leading zeros).
"""


def main():
    # Reads in the first 12 digits of an ISBN-13 number.
    isbn13 = input("\nEnter the first 12-digits of an ISBN-13 number: ")

    # Prints an error message and terminates the program if the length of the user input is not 12.
    if len(isbn13) != 12:
        print("Invalid input, Enter 12 digits.")
        exit(1)

    # Creates variables that stores the odd and even positioned numbers as strings.
    evenDigits = isbn13[::2]
    oddDigits = isbn13[1::2]

    sumOfEvenDigits = sumOfOddDigits = 0

    # Determines the sum of the odd and even positioned numbers.
    for i in range(len(evenDigits)):
        sumOfEvenDigits += 3 * int(evenDigits[i])
        sumOfOddDigits += int(oddDigits[i])

    # Determines the CheckSum
    checkSum = 10 - (sumOfOddDigits + sumOfEvenDigits) % 10

    # Displays the result based on the value of the checkSum.
    if checkSum == 10:
        print(f"\nThe ISBN-13 number is: {isbn13 + '0'}")
    else:
        print(f"\nThe ISBN-13 number is: {isbn13 + str(checkSum)}")


if __name__ == "__main__":
    main()
