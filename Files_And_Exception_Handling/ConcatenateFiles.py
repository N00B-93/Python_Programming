from sys import argv
from os.path import exists

"""
    This is a program that concatenates the contents of several files into another file. The files to be concatenated
    are taken as command line arguments.
"""


def main():
    # Displays a usage message and terminates the program if the number of command line arguments are less than 4.
    if len(argv) < 4:
        print("\nUsage: python ConcatenateFiles.py file1 file2 ... fileN destinationFile")
        exit(1)

    # Creates the destination file if it doesn't exist.
    if not exists(argv[len(argv) - 1]):
        with open(argv[len(argv) - 1], "w") as fileHandler:
            pass
    else:  # Exits the program if the destination already exists.
        print(f"\nThe destination file {argv[len(argv) - 1]} already exists and cannot be overwritten!!!")
        exit(2)

    try:
        # Loop that reads the content out of each source files and writes the content into the destination file.
        for i in range(1, len(argv) - 1):
            with open(argv[i]) as fileHandler1, open(argv[len(argv) - 1], "a") as fileHandler2:
                fileContent = fileHandler1.read()

                fileHandler2.write(fileContent)
        print("\n Contents of the source successfully concatenated into the destination file!!!")
    except FileNotFoundError as fileNotFoundError:
        print(fileNotFoundError.__str__())
    except Exception as exception:
        print(exception.__str__())


if __name__ == "__main__":
    main()
