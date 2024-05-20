"""
    This is a program that prompts the user to enter his/her password and then verifies if the password
    is secure or not. A secure password follows the following rules;
                • The password must be at least 8 characters long.
                • The password must have at least one uppercase and one lowercase letter.
                • The password must have at least one digit
"""


def countUppercaseLetters(password: str) -> int:
    """
    This is a function that counts the number of uppercase characters present in a String.

    :param password: (str) The String to be processed.

    :return: (int) The number of uppercase letters present in a String.
    """
    numberOfUppercaseLetters: int = 0

    for _ in password:
        if _.isupper():
            numberOfUppercaseLetters += 1
    return numberOfUppercaseLetters


def countLowerLetters(password: str) -> int:
    """
    This is a function that counts the number of lowercase characters present in a String.

    :param password: (str) The String to be processed.

    :return: (int) The number of lowercase letters present in a String.
    """
    numberOfLowercaseLetters: int = 0

    for _ in password:
        if _.islower():
            numberOfLowercaseLetters += 1
    return numberOfLowercaseLetters


def countNumbers(password: str) -> int:
    """
    This is a function that counts the number of digits present in a String.

    :param password: (str) The String to be processed.

    :return: (int) The number of digits present in a String.
    """
    numberOfDigits: int = 0

    for _ in password:
        if _.isdigit():
            numberOfDigits += 1
    return numberOfDigits


def isSecure(password: str) -> bool:
    """
    Checks if a password is secure or not a password is secure if; (a) It is at least 8 characters long, 
    (b) Contains at least one uppercase and one lowercase character, (c) Contains at least one digit.

    :param password: (str) The password to be checked.

    :return: (bool) True if the password is secure, else False.
    """
    if (len(password) >= 8 and countNumbers(password) >= 1 and countUppercaseLetters(password) >= 1 and
            countLowerLetters(password) >= 1):
        return True
    return False


def main() -> None:
    # Prompts the user to enter his/her password.
    password: str = input("\nEnter your password: ").strip()

    # Checks if the user's password is secure or not.
    if isSecure(password):
        print(f"\n{password} is a secure Password!")
    else:
        print(f"\n{password} is not a secure Password!")


if __name__ == "__main__":
    main()
