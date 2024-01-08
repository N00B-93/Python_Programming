import sqlite3

"""
    This is a program that creates a database named studentInfo.db which contains three tables;
    1. Major Table with the following columns:
        - Major ID
        - Major Name
    2. Department Table with the following columns:
        - Department ID
        - Department Name
    3. Student Table with the following columns:
        - Student ID
        - Student Name
        - Major ID
        - Department ID 
"""

connection = None

try:
    # Creates a connectio.
    connection = sqlite3.connect('studentInfo.db')

    # Creates a Cursor Object.
    connectionCursor = connection.cursor()

    # SQL Query to create the Major table.
    sqlQuery1 = "CREATE TABLE IF NOT EXISTS Major(MajorID INTEGER PRIMARY KEY AUTOINCREMENT, MajorName TEXT)"

    # Executes the SqlQuery1
    connectionCursor.execute(sqlQuery1)

    # SQL Query that creates the Department table.
    sqlQuery2 = "CREATE TABLE IF NOT EXISTS Department(DepartmentID INTEGER PRIMARY KEY, DepartmentName TEXT)"

    # Executes the sqlQuery2
    connectionCursor.execute(sqlQuery2)

    # SQL Query that creates the Student table.
    sqlQuery3 = """CREATE TABLE IF NOT EXISTS Student(StudentID INTEGER PRIMARY KEY, StudentName TEXT,
                    MajorID INTEGER, DepartmentID INTEGER, FOREIGN KEY(MajorID) References Major(MajorID),
                    FOREIGN KEY(DepartmentID) REFERENCES Department(DepartmentID))"""

    # Executes the sqlQuery3
    connectionCursor.execute(sqlQuery3)

    # Commit changes to the Database.
    connection.commit()

    # Display a message to indicate that the Database and Tables has been created.
    print("\nDatabase and Tables created successfully")
except sqlite3.Error as error:
    print(error)
except Exception as error:
    print(error)
finally:
    if connection is not None:
        connection.close()
