import sqlite3
from sys import exit


def addNewStudent():
    connection = None

    try:
        connection = sqlite3.connect('studentInfo.db')

        connectionCursor = connection.cursor()

        sqlQuery = """INSERT INTO Student(StudentID, StudentName, MajorID, DepartmentID) VALUES (?, ?, ?, ?)"""

        studentID = int(input("\nEnter Student ID: "))
        studentName = input("\nEnter Student name: ")
        majorID = int(input("\nEnter MajorID: "))
        departmentID = int(input("\nEnter DepartmentID: "))

        connectionCursor.execute(sqlQuery, (studentID, studentName, majorID, departmentID))

        connection.commit()

        print(f"\n{studentName} added successfully!")
    except sqlite3.Error as error:
        print(f"\n{error}")
    except Exception as error:
        print(f"\n{error}")
    finally:
        if connection is not None:
            connection.close()


def searchExistingStudents():
    connection = None

    try:
        connection = sqlite3.connect('studentInfo.db')

        connectionCursor = connection.cursor()

        sqlQuery = """SELECT * FROM Student WHERE StudentID=?"""

        studentID = int(input("\nEnter Student ID: "))

        connectionCursor.execute(sqlQuery, (studentID,))

        student = connectionCursor.fetchall()

        if not student:
            print("\nNo such Student!")
            connection.close()
            return

        print("\nStudent Found!")

        print(f"\nStudent ID: {student[0][0]}\nStudent Name: {student[0][1]}\n"
              f"Major ID: {student[0][2]}\nDepartment ID: {student[0][3]}")
    except sqlite3.Error as error:
        print(f"\n{error}")
    except Exception as error:
        print(f"\n{error}")
    finally:
        if connection is not None:
            connection.close()


def updateExistingStudent():
    connection = None

    try:
        connection = sqlite3.connect('studentInfo.db')

        connectionCursor = connection.cursor()

        sqlQuery = """UPDATE Student SET StudentID = ?, StudentName = ?, MajorID = ?, DepartmentID = ? 
                    WHERE StudentID = ?"""

        studentID = int(input("\nEnter Student ID: "))
        newStudentID = int(input("\nEnter new StudentID: "))
        newStudentName = input("\nEnter new Student Name: ")
        newStudentMajorID = input("\nEnter new Student Major ID: ")
        newStudentDepartmentID = input("\nEnter new Student DepartmentID: ")

        connectionCursor.execute(sqlQuery, (newStudentID, newStudentName,
                                            newStudentMajorID, newStudentDepartmentID, studentID))

        if connectionCursor.rowcount == 1:
            print('\nStudent details updated successfully!')
        else:
            print('\nStudent details not updated, Try again.')

        connection.commit()
    except sqlite3.Error as error:
        print(error)
    except Exception as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()


def deleteExistingStudent():
    connection = None

    try:
        connection = sqlite3.connect('studentInfo.db')

        connectionCursor = connection.cursor()

        sqlQuery = "DELETE FROM Student WHERE StudentID = ?"

        studentID = int(input("\nEnter student ID: "))

        connectionCursor.execute(sqlQuery, (studentID,))

        connection.commit()

        if connectionCursor.rowcount == 1:
            print('\nStudent details deleted successfully!')
        else:
            print('\nStudent details not deleted, Try again.')
    except sqlite3.Error as error:
        print(error)
    except Exception as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()


def showAllStudents():
    connection = None

    try:
        connection = sqlite3.connect('studentInfo.db')

        connectionCursor = connection.cursor()

        sqlQuery = "SELECT * FROM Student"

        connectionCursor.execute(sqlQuery)

        students = connectionCursor.fetchall()

        print("\n\t\t\t\tList of Students")
        print("\nStudentID\t\tStudentName\t\t\t\tMajorID\t\tDepartmentID")

        for student in students:
            print(f"{student[0]:9}\t\t{student[1]:30}{student[2]:1}\t\t\t\t{student[3]}")
    except sqlite3.Error as error:
        print(error)
    except Exception as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()


def main():
    while True:
        print("\nWhat would you like to do?\n1. Add new Student\n2. Search for existing Student\n"
              "3. Update student details\n4. Delete student details\n5. Show All Students\n6. Exit")
        choice = input("\nEnter your choice: ")

        match choice:
            case '1':
                addNewStudent()
                choice = input("\nWould you like to continue? ('y' for yes, 'n' for no): ")
                if choice == 'y':
                    continue
                else:
                    exit(0)
            case '2':
                searchExistingStudents()
                choice = input("\nWould you like to continue? ('y' for yes, 'n' for no): ")
                if choice == 'y':
                    continue
                else:
                    exit(0)
            case '3':
                updateExistingStudent()
                choice = input("\nWould you like to continue? ('y' for yes, 'n' for no): ")
                if choice == 'y':
                    continue
                else:
                    exit(0)
            case '4':
                deleteExistingStudent()
                choice = input("\nWould you like to continue? ('y' for yes, 'n' for no): ")
                if choice == 'y':
                    continue
                else:
                    exit(0)
            case '5':
                showAllStudents()
                choice = input("\nWould you like to continue? ('y' for yes, 'n' for no): ")
                if choice == 'y':
                    continue
                else:
                    exit(0)
            case '6':
                print('\nExiting...')
                exit(0)
            case _:
                print('\nInvalid Input!')


if __name__ == "__main__":
    main()
