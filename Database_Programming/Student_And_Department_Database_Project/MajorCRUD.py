import sqlite3
from sys import exit


def createMajor():
    connection = None

    try:
        connection = sqlite3.connect('studentInfo.db')

        connectionCursor = connection.cursor()

        sqlQuery = "INSERT INTO Major(MajorID, MajorName) VALUES(?, ?)"

        majorID = int(input("\nEnter Major ID: "))

        majorName = input("\nEnter Major Name: ")

        connectionCursor.execute(sqlQuery, (majorID, majorName))

        connection.commit()

        print("\n{majorName} Major created successfully".format(majorName=majorName))
    except sqlite3.Error as error:
        print(error)
    except Exception as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()
    return


def searchMajor():
    connection = None

    try:
        connection = sqlite3.connect('studentInfo.db')

        connectionCursor = connection.cursor()

        sqlQuery = "SELECT MajorName FROM Major WHERE MajorID = ?"

        majorID = int(input("\nEnter Major ID: "))

        connectionCursor.execute(sqlQuery, (majorID,))

        print(f"\nMajor Found!\n\nMajor Name: {connectionCursor.fetchone()[0]}")

        connection.commit()
    except sqlite3.Error as error:
        print(error)
    except Exception as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()
    return


def updateMajor():
    connection = None

    try:
        connection = sqlite3.connect('studentInfo.db')

        connectionCursor = connection.cursor()

        sqlQuery = "UPDATE Major SET MajorName = ? WHERE MajorID = ?"

        majorID = int(input("\nEnter the ID of the Major to be updated: "))

        majorName = input("\nEnter the new Major name: ")

        connectionCursor.execute(sqlQuery, (majorName, majorID))

        print("\nMajor Updated Successfully!")

        connection.commit()
    except sqlite3.Error as error:
        print(error)
    except Exception as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()
    return


def deleteMajor():
    connection = None

    try:
        connection = sqlite3.connect('studentInfo.db')

        connectionCursor = connection.cursor()

        sqlQuery = "DELETE FROM Major WHERE MajorID = ?"

        majorID = int(input("\nEnter the ID of the Major to be deleted: "))

        connectionCursor.execute(sqlQuery, (majorID, ))

        print("\nMajor Deleted Successfully!")

        connection.commit()
    except sqlite3.Error as error:
        print(error)
    except Exception as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()
    return


def showAllMajors():
    connection = None

    try:
        connection = sqlite3.connect('studentInfo.db')

        connectionCursor = connection.cursor()

        sqlQuery = "SELECT * FROM Major "

        connectionCursor.execute(sqlQuery)

        majors = connectionCursor.fetchall()

        print("\nMajorID\t\tMajorName")
        for major in majors:
            print(f"\n{major[0]:5}\t\t{major[1]:30}")

    except sqlite3.Error as error:
        print(error)
    except Exception as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()


def main():
    while True:
        print("\nWhat would you like to do?\n1. Add new Major\n2. Search Existing Major\n3. Update an existing Major\n"
              "4. Delete an existing Major\n5. Show all Majors\n6. Exit")
        choice = input("\nEnter your choice: ")

        match choice:
            case '1':
                createMajor()
                choice = input("\nWould you like to continue? ('y' for yes, 'n' for no): ")
                if choice == 'y':
                    continue
                else:
                    exit(0)
            case '2':
                searchMajor()
                choice = input("\nWould you like to continue? ('y' for yes, 'n' for no): ")
                if choice == 'y':
                    continue
                else:
                    exit(0)
            case '3':
                updateMajor()
                choice = input("\nWould you like to continue? ('y' for yes, 'n' for no): ")
                if choice == 'y':
                    continue
                else:
                    exit(0)
            case '4':
                deleteMajor()
                choice = input("\nWould you like to continue? ('y' for yes, 'n' for no): ")
                if choice == 'y':
                    continue
                else:
                    exit(0)
            case '5':
                showAllMajors()
                choice = input("\nWould you like to continue? ('y' for yes, 'n' for no): ")
                if choice == 'y':
                    continue
                else:
                    exit(0)
            case '6':
                print("\nExiting...")
                exit(0)


if __name__ == '__main__':
    main()
