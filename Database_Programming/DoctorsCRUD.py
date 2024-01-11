import sqlite3
from sys import exit


def addNewDoctor():
    connection = None

    try:
        connection = sqlite3.connect('hospital.db')

        connectionCursor = connection.cursor()

        sqlQuery = """INSERT INTO Doctors(DoctorID, DoctorName, HospitalID, JoiningDate, Speciality, Salary, Experience) 
        VALUES(?, ?, ?, ?, ?, ?, ?) """

        doctorID = int(input("\nEnter DoctorID: "))
        doctorName = input("\nEnter Doctor's Name: ")
        hospitalID = int(input("\nEnter HospitalID: "))
        joiningDate = input("\nEnter Joining Date (dd/mm/yyyy): ")
        speciality = input("\nEnter Speciality: ")
        salary = float(input("\nEnter Salary: $ "))
        experience = input("\nEnter Years of Experience: ")

        connectionCursor.execute(sqlQuery, (doctorID, doctorName, hospitalID, joiningDate,
                                            speciality, salary, experience))
        connection.commit()
        if connectionCursor.rowcount == 1:
            print(f"\nDoctor {doctorName} Added Successfully!")
        else:
            print("\nDoctor not Added, Try again.")
    except sqlite3.Error as error:
        print(error)
    except Exception as error:
        print(error)
    finally:
        if connection:
            connection.close()
    return


def searchExistingDoctor():
    connection = None

    try:
        connection = sqlite3.connect('hospital.db')

        connectionCursor = connection.cursor()

        sqlQuery = """SELECT * FROM Doctors WHERE DoctorID = ? """

        doctorID = int(input("\nEnter DoctorID: "))

        connectionCursor.execute(sqlQuery, (doctorID,))

        doctor = connectionCursor.fetchone()

        if not doctor:
            print("\nDoctor not found")
            connection.close()
            return
        print("\nDoctor Found!\n")
        print(f"\nDoctorID: {doctor[0]}\nDoctor Name: {doctor[1]}\nHospitalID: {doctor[2]}\nJoining Date: {doctor[3]}\n"
              f"Speciality: {doctor[4]}\nSalary: $ {doctor[5]}\nExperience: {doctor[6]}")
    except sqlite3.Error as error:
        print(error)
    except Exception as error:
        print(error)
    finally:
        if connection:
            connection.close()
    return


def updateDoctorDetails():
    connection = None

    try:
        connection = sqlite3.connect('hospital.db')

        connectionCursor = connection.cursor()

        doctorID = int(input("\nEnter DoctorID: "))

        detail = ""

        print("\nWhat would you like to update?\n1. Doctor Name\n2. Doctor ID\n3. HospitalID\n4. Salary\n"
              "5. Experience\n6. Joining Date\n")
        choice = input("\nEnter your choice: ")

        match choice:
            case '1':
                newName = input("\nEnter New Name: ")
                sqlQuery = """UPDATE Doctors SET DoctorName = ? WHERE DoctorID = ?"""
                connectionCursor.execute(sqlQuery, (newName, doctorID))
                detail = "Name"
            case '2':
                newID = input("\nEnter new ID: ")
                sqlQuery = """UPDATE Doctors SET DoctorID = ? WHERE DoctorID = ?"""
                connectionCursor.execute(sqlQuery, (newID, doctorID))
                detail = "DoctorID"
            case '3':
                newHospitalID = input("\nEnter new HospitalID: ")
                sqlQuery = "UPDATE Doctors SET HospitalID = ? WHERE DoctorID = ?"
                connectionCursor.execute(sqlQuery, (newHospitalID, doctorID))
                detail = "HospitalID"
            case '4':
                newSalary = input("\nEnter new Salary: $ ")
                sqlQuery = """UPDATE Doctors SET Salary = ? WHERE DoctorID = ?"""
                connectionCursor.execute(sqlQuery, (newSalary, doctorID))
                detail = "Salary"
            case '5':
                newExperience = input("\nEnter new Years of Experience: ")
                sqlQuery = """UPDATE Doctors SET Experience = ? WHERE DoctorID = ?"""
                connectionCursor.execute(sqlQuery, (newExperience, doctorID))
                detail = "Experience"
            case '6':
                newJoinDate = input("\nEnter new Joining Date: ")
                sqlQuery = """UPDATE Doctors SET Doctors.JoiningDate = ? WHERE DoctorID = ?"""
                connectionCursor.execute(sqlQuery, (newJoinDate, doctorID))
                detail = "Joining Date"

        if connectionCursor.rowcount == 1:
            print(f"\n{detail} Updated Successfully!")
            connection.commit()
        else:
            print("\nDetail Not Updated!")
            connection.close()
            return
    except sqlite3.Error as error:
        print(error)
    except Exception as error:
        print(error)
    finally:
        if connection:
            connection.close()
    return


def deleteDoctor():
    connection = sqlite3.connect('hospital.db')

    try:
        connectionCursor = connection.cursor()

        sqlQuery = """DELETE FROM Doctors WHERE DoctorID = ?"""

        doctorID = int(input("\nEnter Doctor ID: "))

        connectionCursor.execute(sqlQuery, (doctorID, ))

        connection.commit()

        if connectionCursor.rowcount == 1:
            print("\nDoctor details Deleted Successfully!")
        else:
            print("\nDetail Not Deleted!")
            connection.close()
            return
    except sqlite3.Error as error:
        print(error)
    except Exception as error:
        print(error)
    finally:
        if connection:
            connection.close()
    return


def showAllDoctors():
    connection = None

    try:
        connection = sqlite3.connect('hospital.db')

        connectionCursor = connection.cursor()

        sqlQuery = "SELECT * FROM Doctors"

        connectionCursor.execute(sqlQuery)

        doctors = connectionCursor.fetchall()

        for doctor in doctors:
            print(f"Doctor ID: {doctor[0]}\nDoctor Name: {doctor[1]}\nHospital ID: {doctor[2]}"
                  f"\nJoined Date: {doctor[3]}\nSpeciality: {doctor[4]}\nSalary: $ {doctor[5]}\n"
                  f"Years of Experience: {doctor[6]}\n")
    except sqlite3.Error as error:
        print(error)
    except Exception as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()
    return


def main():
    while True:
        print("\nWhat would you like to do?\n1. Add a new Doctor\n2. Search for a Doctor\n3. Update Doctor Details\n"
              "4. Delete a Doctor\n5. Show All Doctors\n6. Exit")
        choice = input("\nEnter your choice: ")

        match choice:
            case '1':
                addNewDoctor()
                choice = input("\nWould you like to continue? ('y' for yes, 'n' for no): ")
                if choice == 'y':
                    continue
                else:
                    exit(0)
            case '2':
                searchExistingDoctor()
                choice = input("\nWould you like to continue? ('y' for yes, 'n' for no): ")
                if choice == 'y':
                    continue
                else:
                    exit(0)
            case '3':
                updateDoctorDetails()
                choice = input("\nWould you like to continue? ('y' for yes, 'n' for no): ")
                if choice == 'y':
                    continue
                else:
                    exit(0)
            case '4':
                deleteDoctor()
                choice = input("\nWould you like to continue? ('y' for yes, 'n' for no): ")
                if choice == 'y':
                    continue
                else:
                    exit(0)
            case '5':
                showAllDoctors()
                choice = input("\nWould you like to continue? ('y' for yes, 'n' for no): ")
                if choice == 'y':
                    continue
                else:
                    exit(0)
            case '6':
                print("\nExiting...")
                exit(0)
            case _:
                print("\nInvalid Input, Try Again...")


if __name__ == "__main__":
    main()
