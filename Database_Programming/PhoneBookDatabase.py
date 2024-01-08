import sqlite3

"""
    This is a program that creates a database named phonebook.db. The database has
    a table named Entries, with columns for a person’s name and phone number.
"""
# Initializes a connection Object to None.
connection = None

try:
    # Creates a connection Object.
    connection = sqlite3.connect('phonebook.db')

    # Creates a connection Cursor
    connectionCursor = connection.cursor()

    # SQL Query to be executed.
    sqlQuery = "CREATE TABLE IF NOT EXISTS Entries(Name TEXT, PhoneNumber TEXT)"

    # Executes the SQL query.
    connectionCursor.execute(sqlQuery)

    # Commit changes to the database.
    connection.commit()

    print("\nDatabase Created Successfully!")
except sqlite3.Error as error:
    # Displays an error message if an error is encountered while trying to execute the query.
    print(error)
finally:
    # Close the connection.
    connection.close()
