from pickle import load, dump
from os.path import exists

"""
     This is an email database management system that allows users to perform various operations such as adding, 
     searching, updating, deleting, and displaying email addresses associated with names.
"""


def addNameAndEmail() -> None:
    with open("namesAndEmails.pickle", "rb") as fileHandler:
        namesAndEmails: dict = load(fileHandler)

    # Prompts the user to enter the name and email to be added.
    name: str = input("\nEnter Name: ").title()
    email: str = input("\nEnter Email: ")

    # Adds the name and email entered by the user to the namesAndEmails dictionary.
    namesAndEmails[name] = email
    print("\nData added Successfully.")

    # Writes the data to a file.
    with open("namesAndEmails.pickle", "wb") as fileHandler:
        dump(namesAndEmails, fileHandler)
    return


def searchEmail() -> None:
    # Reads in a name whose email is required and converts it to lower case.
    name: str = input("\nEnter Name: ").title()

    # Reads the data from the names and emails database into a dictionary.
    with open("namesAndEmails.pickle", "rb") as fileHandler:
        namesAndEmails: dict = load(fileHandler)

    try:
        # Displays the user's email.
        if name in namesAndEmails.keys():
            print("\nEmail found!")
            print(f"\nEmail: {namesAndEmails[name]}")
        else:
            print(f"\n{name.title()} not found in database!!!")
    except KeyError:
        raise KeyError("Email not found, Try again.")
    return


def updateEmail() -> None:
    # Reads in the user's name.
    name = input("\nEnter Name: ").title()

    # Reads the data from the names and emails database into a dictionary.
    with open("namesAndEmails.pickle", "rb") as fileHandler:
        namesAndEmails: dict = load(fileHandler)

    # Returns to the caller if the name is not in the database.
    if name not in namesAndEmails.keys():
        print(f"\n{name} not found!!!")
        return

    # Reads in the user's new email.
    email = input("\nEnter new Email: ")

    # Updates the email.
    namesAndEmails[name] = email
    print("\nEmail Updated Successfully!")

    # Writes the updated data into the database.
    with open("namesAndEmails.pickle", "wb") as fileHandler:
        dump(namesAndEmails, fileHandler)
    return


def deleteNameAndEmail() -> None:
    # Reads in the name to be deleted from the database.
    name = input("\nEnter a name whose details is to be deleted: ").title()

    # Reads the data from the names and emails database into a dictionary.
    with open("namesAndEmails.pickle", "rb") as fileHandler:
        namesAndEmails: dict = load(fileHandler)

    # Returns to the caller if the name is not in the database.
    if name not in namesAndEmails.keys():
        print(f"\n{name} not found!!!")
        return

    # Deletes the name and email from the database.
    namesAndEmails.pop(name)
    print("\nData deleted Successfully!")

    # Writes the updated data into the database.
    with open("namesAndEmails.pickle", "wb") as fileHandler:
        dump(namesAndEmails, fileHandler)

    return


def showAllContacts() -> None:
    # Reads the data from the file.
    with open("namesAndEmails.pickle", "rb") as fileHandler:
        namesAndEmails: dict = load(fileHandler)

    # Informs the user that the database is empty if there is no entry in the database.
    if len(namesAndEmails) == 0:
        print("\nDatabase is empty.")
        return

    # Displays all the name and emails in the database.
    for name, email in namesAndEmails.items():
        print(f"\nName: {name}\nEmail: {email}")


def main() -> None:
    # Creates a dictionary that stores names and emails as key, value pairs.
    namesAndEmails: dict = {}

    if not exists("namesAndEmails.pickle"):
        # Creates a file to store names and emails.
        with open("namesAndEmails.pickle", "wb") as fileHandler:
            dump(namesAndEmails, fileHandler)

    while True:
        # Displays the menu.
        print("""
                \n\t\tWelcome to $N00B's Email Database!
                \nWhat would you like to do?
                \n1. Add a name and email address
                \n2. Search for a name and email address
                \n3. Update a name and email address
                \n4. Delete a name and email address
                \n5. Display all names and email addresses
                \n6. Exit
        """)
        # Reads in the user's choice.
        choice: str = input("\nEnter your choice: ")

        match choice:
            case "1":
                addNameAndEmail()
                choice = input("\nWould you like to continue('y' or 'n')? ")
                if choice == "y":
                    continue
                else:
                    print("\nExiting...")
                    exit(0)
            case "2":
                try:
                    searchEmail()
                except KeyError as keyError:
                    print(keyError.__str__())
                choice = input("\nWould you like to continue('y' or 'n')? ")
                if choice == "y":
                    continue
                else:
                    print("\nExiting...")
                    exit(0)
            case "3":
                updateEmail()
                choice = input("\nWould you like to continue('y' or 'n')? ")
                if choice == "y":
                    continue
                else:
                    print("\nExiting...")
                    exit(0)
            case "4":
                deleteNameAndEmail()
                choice = input("\nWould you like to continue('y' or 'n')? ")
                if choice == "y":
                    continue
                else:
                    print("\nExiting...")
                    exit(0)
            case "5":
                showAllContacts()
                choice = input("\nWould you like to continue('y' or 'n')? ")
                if choice == "y":
                    continue
                else:
                    print("\nExiting...")
                    exit(0)
            case "6":
                print("\nExiting...")
                exit(0)

            case _:
                print("\nInvalid input, Try again.")

            
if __name__ == "__main__":
    main()
