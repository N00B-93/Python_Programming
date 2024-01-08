import sqlite3
from sys import exit

"""
    This is a CRUD application that lets the user add rows to the Entries table, look up a person’s
    phone number, change a person’s phone number, and delete specified rows.
"""


def addEntry():
    connection = None

    try:
        connection = sqlite3.connect('phonebook.db')
        connectionCursor = connection.cursor()

        sqlQuery = "INSERT INTO Entries VALUES (?, ?)"

        name = input("\nEnter Name: ")
        phoneNumber = input("\nEnter Phone Number: ")

        connectionCursor.execute(sqlQuery, (name, phoneNumber))

        connection.commit()

        print("\nEntry was successfully added!")
    except sqlite3.Error as error:
        print(error)
    except Exception as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()
    return


def searchEntry():
    connection = None

    try:
        connection = sqlite3.connect('phonebook.db')
        connectionCursor = connection.cursor()

        sqlQuery = "SELECT PhoneNumber FROM Entries WHERE lower(Name) == ?"

        name = input("\nEnter Name: ")

        connectionCursor.execute(sqlQuery, (name, ))

        phoneNumber = connectionCursor.fetchone()

        connection.commit()

        print("\nRecord Found!")
        print(f"\nPhoneNumber: {phoneNumber[0]}")
    except sqlite3.Error as error:
        print(error)
    except Exception as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()
    return


def updateEntry():
    connection = None

    try:
        connection = sqlite3.connect('phonebook.db')

        connectionCursor = connection.cursor()

        sqlQuery = "UPDATE Entries SET phoneNumber = ? WHERE lower(Name) == ?"

        name = input("\nEnter Name: ")
        phoneNumber = input("\nEnter new Phone Number: ")

        connectionCursor.execute(sqlQuery, (phoneNumber, name))

        connection.commit()

        print("\nPhone Number was successfully updated!")
    except sqlite3.Error as error:
        print(error)
    except Exception as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()
    return


def deleteEntry():
    connection = None

    try:
        connection = sqlite3.connect('phonebook.db')

        connectionCursor = connection.cursor()

        sqlQuery = "DELETE FROM Entries WHERE lower(Name) == ?"

        name = input("\nEnter name: ")

        connectionCursor.execute(sqlQuery, (name,))

        connection.commit()

        print("\nEntry was successfully deleted!")

    except sqlite3.Error as error:
        print(error)
    except Exception as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()


def main():
    while True:
        print("\nWhat would you like to do?\n1. Add Entry\n2. Search Entry\n3. Update Entry\n4. Delete Entry\n5. Exit")
        choice = input("\nEnter your choice: ")

        match choice:
            case '1':
                addEntry()
                choice = input("\nWould you like to continue? ('y' for yes, 'n' for no): ")
                if choice == 'y':
                    continue
                else:
                    exit(0)
            case '2':
                searchEntry()
                choice = input("\nWould you like to continue? ('y' for yes, 'n' for no): ")
                if choice == 'y':
                    continue
                else:
                    exit(0)
            case '3':
                updateEntry()
                choice = input("\nWould you like to continue? ('y' for yes, 'n' for no): ")
                if choice == 'y':
                    continue
                else:
                    exit(0)
            case '4':
                deleteEntry()
                choice = input("\nWould you like to continue? ('y' for yes, 'n' for no): ")
                if choice == 'y':
                    continue
                else:
                    exit(0)
            case '5':
                print("\nExiting...")
                exit(0)


if __name__ == "__main__":
    main()
