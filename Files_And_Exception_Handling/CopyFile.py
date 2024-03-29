from os.path import exists

"""
    This is a program that prompts the user to enter the name of a source file and the name of a destination file, The
    program then copy the contents of the source file into the destination file.
"""


def main() -> None:
    # Prompts the user to enter the name of the source file.
    srcFile = input("\nEnter the name of the source file: ")

    # Displays an error message and terminates the program if the source file doesn't exist.
    if not exists(srcFile):
        print(f"\nThe file {srcFile} doesn't exist!!!")
        exit(1)

    # Prompts the user to enter the destination file.
    destFile = input("\nEnter the name of the destination file: ")

    # Display an error message and terminates the program if the destination file already exists.
    if exists(destFile):
        print(f"\nThe file {destFile} already exist!!!")
        exit(1)

    try:
        # Opens the source file and read its content.
        with open(srcFile) as fileHandler1:
            srcFileContent = fileHandler1.read()
            # Writes the content of the source file to the destination file.
            with open(destFile, "w") as fileHandler2:
                fileHandler2.write(srcFileContent)
        # Displays a message to inform the user that the content of the file has been copied to the destination
        # successfully.
        print(f"\n{srcFile} successfully copied to {destFile}")
    except IOError as ioError:
        print(ioError.__str__())
    except Exception as exception:
        print(exception.__str__())


if __name__ == "__main__":
    main()
