import sqlite3

# Initializes a Connection Object to None.
connection = None

try:
    # Creates a connection to the hospital.db Database.
    connection = sqlite3.connect('hospital.db')

    # Creates a Cursor Object.
    connectionCursor = connection.cursor()

    # SQL Query that creates the Hospitals table.
    sqlQuery1 = """CREATE TABLE IF NOT EXISTS Hospitals(HospitalID INTEGER PRIMARY KEY, HospitalName TEXT, 
                BedCount INTEGER)"""
    # Executes sqlQuery1.
    connectionCursor.execute(sqlQuery1)

    # SQL Query that creates the Doctors table.
    sqlQuery2 = """CREATE TABLE IF NOT EXISTS Doctors(DoctorID INTEGER PRIMARY KEY, DoctorName TEXT, HospitalID INTEGER,
                JoiningDate TEXT, Speciality TEXT, Salary DOUBLE, Experience INTEGER, FOREIGN KEY(HospitalID) 
                REFERENCES Hospitals(HospitalID))"""
    # Executes sqlQuery2.
    connectionCursor.execute(sqlQuery2)

    # Commits changes to the database.
    connection.commit()

    # Announces the creation of the hospital.db database, Hospitals and Doctors table.
    print("\nHospital Database, Hospitals and Doctors Table created successfully!")
except sqlite3.Error as error:
    print(error)
except Exception as error:
    print(error)
finally:
    # Closes the connection to the database.
    if connection:
        connection.close()
