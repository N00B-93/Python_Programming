"""
    This is a program that prompts the user to enter a phone number as a string. The
    input number may contain letters. The program translates a letter (uppercase or
    lowercase) to a digit and leaves all other characters intact.
"""


def getNumber(letter):
    """
    Returns the numeric value of the given letter.

    :param uppercaseLetter: (str) The letter whose numeric value should be returned.

    :return: (str) The numeric value of the given letter.
    """
    if letter in "abcABC":
        return "2"
    elif letter in "defDEF":
        return "3"
    elif letter in "ghiGHI":
        return "4"
    elif letter in "jklJKL":
        return "5"
    elif letter in "mnoMNO":
        return "6"
    elif letter in "pqrsPQRS":
        return "7"
    elif letter in "tuvTUV":
        return "8"
    elif letter in "wxyzWXYZ":
        return "9"
    return ""

def main():
    # Reads in a phone Number.
    phoneNumber = input("\nEnter your phone number: ")

    # Displays an error message and continue to loop if the user enters an empty string.
    while phoneNumber == "":
        print("\nError: Use non empty strings as phone number only, Try again.")
        phoneNumber = input("\nEnter your phone number: ")

    # Initializes a newPhoneNumber variable as a string.
    newPhoneNumber = ""

    # Replace the occurrence of a letter in the phone number with a variable and concatenate it to the new phone Number.
    for character in phoneNumber:
        if character.isnumeric():
            newPhoneNumber += character
        elif character.isalpha():
            newPhoneNumber += getNumber(character)
        else:
            newPhoneNumber += character

    # Displays the result.
    print(f"\nPhone Number: {newPhoneNumber}")


if __name__ == "__main__":
    main()
