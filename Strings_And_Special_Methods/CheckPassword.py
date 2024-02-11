"""
    This is a program that checks whether a string is a valid password. Suppose the password
    rules are as follows:
        ■ A password must have at least eight characters.
        ■ A password must consist of only letters and digits.
        ■ A password must contain at least two digits.
"""


def validLength(password):
    """
    Returns True if the length of a password is greater than or equal to 8, else returns False.

    :param password: (str) The password to check.

    :return: (bool) True if the length of the password is >= 8, else false.
    """
    if len(password) >= 8:
        return True
    return False


def numberOfDigits(password):
    """
    Returns the number of digits in the password.

    :param password: (str) The password to be checked.

    :return: (int) The number of digits in the password.
    """
    digits = 0

    for character in password:
        if 48 <= ord(character) <= 57:
            digits += 1
    return digits


def main():
    # Reads in a password to be checked.
    password = input("\nEnter your password: ")

    # Checks whether the password is valid or not and displays the result.
    if validLength(password) and numberOfDigits(password) >= 2 and password.isalnum():
        print("\nValid Password!")
    else:
        print("\nInvalid Password!")


if __name__ == "__main__":
    main()
