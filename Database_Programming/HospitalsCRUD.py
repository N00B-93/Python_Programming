import sqlite3
from sys import exit


def addNewHospital():
    connection = None

    try:
        connection = sqlite3.connect('Hospital.db')

        connectionCursor = connection.cursor()

        sqlQuery = """INSERT INTO Hospitals(HospitalID, HospitalName, BedCount) VALUES(?, ?, ?)"""

        hospitalID = int(input("\nEnter Hospital ID: "))
        hospitalName = input("\nEnter Hospital Name: ")
        bedCount = int(input("\nEnter Bed Count: "))

        connectionCursor.execute(sqlQuery, (hospitalID, hospitalName, bedCount))

        connection.commit()

        if connectionCursor.rowcount == 1:
            print(f"\n{hospitalName} Hospital added successfully!")
        else:
            print(f"\n{hospitalName} not added, Try again.")
    except sqlite3.Error as error:
        print(f"\n{error}")
    except Exception as error:
        print(f"\n{error}")
    finally:
        if connection:
            connection.close()


def searchExistingHospital():
    connection = None

    try:
        connection = sqlite3.connect('hospital.db')

        connectionCursor = connection.cursor()

        sqlQuery = """SELECT * FROM Hospitals WHERE HospitalID = ? """

        hospitalID = input("\nEnter HospitalID: ")

        connectionCursor.execute(sqlQuery, (hospitalID,))

        hospital = connectionCursor.fetchone()

        if not hospital:
            print("\nHospital not found")
            connection.close()
            return

        print(f"\nHospital ID: {hospital[0]}\nHospital Name: {hospital[1]}\nNumber of Beds: {hospital[2]}")
    except sqlite3.Error as error:
        print(f"\n{error}")
    except Exception as error:
        print(f"\n{error}")
    finally:
        if connection:
            connection.close()


def updateHospital():

    try:
        connection = sqlite3.connect('hospital.db')

        connectionCursor = connection.cursor()

        print("\nWhat would you like to update?\n1. Hospital Name\n2. Bed Count")
        choice = input("\nSelect an option: ")

        match choice:
            case '1':
                hospitalID = input("\nEnter Hospital ID: ")
                hospitalName = input("\nEnter new Hospital Name: ")
                sqlQuery = """UPDATE Hospitals SET HospitalName = ? WHERE HospitalID = ?"""
                connectionCursor.execute(sqlQuery, (hospitalName, hospitalID))
                if connectionCursor.rowcount == 1:
                    print(f"\nHospital Name changed to {hospitalName}!")
                    connection.commit()
                else:
                    print(f"\nHospital name not changed to {hospitalName}, Try again.")
                    connection.close()
                    return
            case '2':
                hospitalID = input("\nEnter Hospital ID: ")
                bedCount = input("\nEnter new Hospital bed count: ")
                sqlQuery = """UPDATE Hospitals SET BedCount = ? WHERE HospitalID = ?"""
                connectionCursor.execute(sqlQuery, (bedCount, hospitalID))
                if connectionCursor.rowcount == 1:
                    print(f"\nHospital bed count changed to {bedCount}!")
                    connection.commit()
                else:
                    print(f"\nHospital bed count not changed, Try again.")
                    connection.close()
                    return
    except sqlite3.Error as error:
        print(error)
    except Exception as error:
        print(error)


def deleteHospital():
    connection = None

    try:
        connection = sqlite3.connect('hospital.db')

        connectionCursor = connection.cursor()

        sqlQuery = "DELETE FROM Hospitals WHERE HospitalID = ?"

        hospitalID = int(input("\nEnter HospitalID: "))

        connectionCursor.execute(sqlQuery, (hospitalID, ))

        if connectionCursor.rowcount == 1:
            print(f"\nHospital with ID {hospitalID} deleted successfully!")
            connection.commit()
        else:
            print(f"\nHospital with ID {hospitalID} not deleted, Try again.")
            connection.close()
            return
    except sqlite3.Error as error:
        print(error)
    except Exception as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()
    return


def showAllHospitals():
    connection = None

    try:
        connection = sqlite3.connect('hospital.db')

        connectionCursor = connection.cursor()

        sqlQuery = "SELECT * FROM Hospitals"

        connectionCursor.execute(sqlQuery)

        hospitals = connectionCursor.fetchall()

        for hospital in hospitals:
            print(f"\nHospitalID: {hospital[0]}\nHospital Name: {hospital[1]}\nBed Count: {hospital[2]}")
    except sqlite3.Error as error:
        print(error)
    except Exception as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()


def main():
    while True:
        print("\nWhat would you like to do?\n1. Add a new Hospital\n2. Search for an Hospital\n3. Update Hospital "
              "Details\n4. Delete an Hospital\n5. Show All Hospitals\n6. Exit")
        choice = input("\nEnter your choice: ")

        match choice:
            case '1':
                addNewHospital()
                choice = input("\nWould you like to continue? ('y' for yes, 'n' for no): ")
                if choice == 'y':
                    continue
                else:
                    exit(0)
            case '2':
                searchExistingHospital()
                choice = input("\nWould you like to continue? ('y' for yes, 'n' for no): ")
                if choice == 'y':
                    continue
                else:
                    exit(0)
            case '3':
                updateHospital()
                choice = input("\nWould you like to continue? ('y' for yes, 'n' for no): ")
                if choice == 'y':
                    continue
                else:
                    exit(0)
            case '4':
                deleteHospital()
                choice = input("\nWould you like to continue? ('y' for yes, 'n' for no): ")
                if choice == 'y':
                    continue
                else:
                    exit(0)
            case '5':
                showAllHospitals()
                choice = input("\nWould you like to continue? ('y' for yes, 'n' for no): ")
                if choice == 'y':
                    continue
                else:
                    exit(0)
            case '6':
                print("\nExiting...")
                exit(0)
            case _:
                print("\nInvalid Input, try Again!")


if __name__ == "__main__":
    main()
