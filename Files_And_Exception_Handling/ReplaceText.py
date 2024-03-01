from os.path import isfile
from sys import exit

"""
    This program prompts the user to enter a file name, a new String and an old String and then replaces all
    the occurrences of the old String with the new String in the file.
"""


def main() -> None:
    # Reads in the file name.
    fileName = input("\nEnter the file nane: ")

    # Exits the program if the file doesn't exist.
    if not isfile(fileName):
        print(f"\n{fileName} doesn't exist!")
        exit(1)

    # Reads in the old String.
    oldString = input("\nEnter the old String: ")

    # Reads in the new String.
    newString = input("\nEnter the new String: ")

    try:
        # Reads the content of the file into the fileContent variable as a String.
        fileContent = ''

        with open(fileName) as fileHandler:
            fileContent = fileHandler.read()
        
        # Replaces all occurrence of oldString with newString.
        fileContent = fileContent.replace(oldString, newString)
        
        # Write the file's content with the new String into the file.
        with open(fileName, 'w') as fileHandler:
            fileHandler.write(fileContent)
        print(f"\n{oldString} changed to {newString}!")
    except Exception as exception:
        raise exception


if __name__ == "__main__":
    main()

