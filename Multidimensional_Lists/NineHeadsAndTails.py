def decimalToBinary(decimal):
    """
    Returns the binary equivalent of a decimal number as a String.

    :param decimal: (int) The decimal number to be converted.

    :return: (str) Binary representation of the given decimal number.
    """
    binary = ""

    while decimal != 0:
        remainder = decimal % 2
        binary += str(remainder)
        decimal //= 2
    return binary[::-1]


def nineBitRepresentation(binaryNumber):
    """
    Returns the 9-bit representation of a given binary number.

    :param binaryNumber: (str) The binary number whose 9-bit representation is required.

    :return: (str) The 9-bit binary representation of a given number.
    """
    if len(binaryNumber) == 9:
        return binaryNumber

    zeroes = ""

    for i in range(9 - len(binaryNumber)):
        zeroes += '0'
    return zeroes + binaryNumber


def main():
    # Reads in a number from 0 to 511.
    decimal = int(input("\nEnter a number in the range 0 - 511: "))
    
    # Terminates the program if the number is not in range 0 to 511.
    if decimal < 0 or decimal > 511:
        print("\nInvalid Input! Try again.")
        exit(1)
    
    # Gets the 9-bit representation of the binary equivalent of the decimal number entered by the user.
    headsAndTails = nineBitRepresentation(decimalToBinary(decimal))

    # Displays 1's and 0's as heads and tails.
    for i in range(1, len(headsAndTails) + 1):
        if headsAndTails[i - 1] == '0':
            print("H ", end="")
        else:
            print("T ", end="")
        if i > 1 and i % 3 == 0:
            print()


if __name__ == "__main__":
    main()
