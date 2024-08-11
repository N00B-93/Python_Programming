import sqlite3
from sys import exit


def createDepartment():
    connection = None

    try:
        connection = sqlite3.connect('studentInfo.db')

        connectionCursor = connection.cursor()

        sqlQuery = "INSERT INTO Department(DepartmentID, DepartmentName) VALUES(?, ?)"

        departmentID = int(input("\nEnter Department ID: "))

        departmentName = input("\nEnter Department Name: ")

        connectionCursor.execute(sqlQuery, (departmentID, departmentName))

        connection.commit()

        print("\n{departmentName} Department created successfully".format(departmentName=departmentName))
    except sqlite3.Error as error:
        print(error)
    except Exception as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()
    return


def searchDepartment():
    connection = None

    try:
        connection = sqlite3.connect('studentInfo.db')

        connectionCursor = connection.cursor()

        sqlQuery = "SELECT DepartmentName FROM Department WHERE DepartmentID = ?"

        departmentID = int(input("\nEnter Department ID: "))

        connectionCursor.execute(sqlQuery, (departmentID,))

        department = connectionCursor.fetchone()

        if not department:
            print("\n No such Department!")
            return

        print(f"\nDepartment Found!\n\nDepartment Name: {department[0]}")

        connection.commit()
    except sqlite3.Error as error:
        print(error)
    except Exception as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()
    return


def updateDepartment():
    connection = None

    try:
        connection = sqlite3.connect('studentInfo.db')

        connectionCursor = connection.cursor()

        sqlQuery = "UPDATE Department SET DepartmentName = ? WHERE DepartmentID = ?"

        departmentID = int(input("\nEnter the ID of the Department to be updated: "))

        departmentName = input("\nEnter the new Department name: ")

        connectionCursor.execute(sqlQuery, (departmentName, departmentID))

        print("\nDepartment Updated Successfully!")

        connection.commit()
    except sqlite3.Error as error:
        print(error)
    except Exception as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()
    return


def deleteDepartment():
    connection = None

    try:
        connection = sqlite3.connect('studentInfo.db')

        connectionCursor = connection.cursor()

        sqlQuery = "DELETE FROM Department WHERE DepartmentID = ?"

        departmentID = int(input("\nEnter the ID of the Department to be deleted: "))

        connectionCursor.execute(sqlQuery, (departmentID, ))

        print("\nDepartment Deleted Successfully!")

        connection.commit()
    except sqlite3.Error as error:
        print(error)
    except Exception as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()
    return


def showAllDepartment():
    connection = None

    try:
        connection = sqlite3.connect('studentInfo.db')

        connectionCursor = connection.cursor()

        sqlQuery = "SELECT * FROM Department "

        connectionCursor.execute(sqlQuery)

        departments = connectionCursor.fetchall()

        print("\nDepartmentID\t\tDepartmentName")
        for department in departments:
            print(f"\n{department[0]:5}\t\t{department[1]:30}")

    except sqlite3.Error as error:
        print(error)
    except Exception as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()


def main():
    while True:
        print("\nWhat would you like to do?\n1. Add new Department\n2. Search Existing Department\n"
              "3. Update an existing Department\n4. Delete an existing Department\n5. Show all Department\n6. Exit")
        choice = input("\nEnter your choice: ")

        match choice:
            case '1':
                createDepartment()
                choice = input("\nWould you like to continue? ('y' for yes, 'n' for no): ")
                if choice == 'y':
                    continue
                else:
                    exit(0)
            case '2':
                searchDepartment()
                choice = input("\nWould you like to continue? ('y' for yes, 'n' for no): ")
                if choice == 'y':
                    continue
                else:
                    exit(0)
            case '3':
                updateDepartment()
                choice = input("\nWould you like to continue? ('y' for yes, 'n' for no): ")
                if choice == 'y':
                    continue
                else:
                    exit(0)
            case '4':
                deleteDepartment()
                choice = input("\nWould you like to continue? ('y' for yes, 'n' for no): ")
                if choice == 'y':
                    continue
                else:
                    exit(0)
            case '5':
                showAllDepartment()
                choice = input("\nWould you like to continue? ('y' for yes, 'n' for no): ")
                if choice == 'y':
                    continue
                else:
                    exit(0)
            case '6':
                print("\nExiting...")
                exit(0)
            case _:
                print("\nInvalid Choice!\n")


if __name__ == '__main__':
    main()
