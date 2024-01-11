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


if __name__ == "__main__":
    main()
