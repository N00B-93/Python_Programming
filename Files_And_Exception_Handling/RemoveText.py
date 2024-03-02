"""
    This is a program that prompts the user to enter a file name and a String to be removed, then removes
    all occurrences of the specified String from the file.
"""


def main() -> None:
    # Prompts the user to enter the name of the file and the String to be removed.
    fileName = input("\nEnter the name of the file: ")
    string = input("\nEnter the String to be removed from the file: ")

    try:
        # Reads the content of the file into a String variable.
        with open(fileName, 'r') as fileHandler:
            fileContent = fileHandler.read()
        
        # Replace all occurrence of the String with an empty String.
        fileContent = fileContent.replace(string, '')
        
        # Write the file content back to the file without the specified String.
        with open(fileName, 'w') as fileHandler:
            fileHandler.write(fileContent)
        print(f"\n{string} removed from the {fileName} file!")
    except IOError as ioError:
        print(ioError)
    except Exception as exception:
        print(exception)


if __name__ == "__main__":
    main()
