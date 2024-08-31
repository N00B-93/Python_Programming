"""
    This is a program that gets a string containing a person’s first, middle, and last names, and 
    displays their first, middle, and last initials. 
"""


def getInitials(fullName: str) -> str:
    """
    This returns the initials given a String representing a fullname.

    parameters:
        fullName (str): The user's first, middle and last names.

    Returns:
        str: A String representing the user's initials.
    """
    fullName = fullName.title()

    names: list = fullName.split()

    if len(names) != 3:
        return ""

    initials = names[0][0] + ". " + names[1][0] + ". " + names[2][0]

    return initials


def main() -> None:
    # Prompts the user to enter his/her full name.
    fullName = input("\nEnter your first, middle and last name(e.g. john peter smith): ").strip()
    
    # Displays an error message and terminates the program if the user enters an empty String.
    if not fullName:
        print("\nError: Use a non-empty String for the full name, Try again.")
        exit(1)
    
    # Determines the user's initials.
    initials: str = getInitials(fullName)
    
    # Displays an error message and terminates the program if the user doesn't enter his/her
    # first, middle or last names.
    if not initials:
        print("\nError: First, middle and last names are all required, Try again.")
        exit(2)
    else:    
        print(f"\nYour initials is: {initials}")


if __name__ == "__main__":
    main()

