from os import rename
from sys import argv
from os.path import exists

"""
    This is a program that replaces all the lines in a file with it's reverse. The name of the file to be
    reversed is taken as a command line argument.
"""


def main() -> None:
    # Displays a usage message if the wrong number of command line argument is used.
    if len(argv) != 2:
        print("\nUsage: python Reverse.py fileName")
        exit(1)

    # Displays an error message and terminates the program if the file to be reversed doesn't exist.
    if not exists(argv[1]):
        print(f"\n{argv[1]} doesn't exists")
        exit(2)

    try:
        # Opens the file in read mode.
        with open(argv[1]) as fileHandler1:
            # Reads out all the contents of the file into a list.
            fileContent: list = fileHandler1.readlines()
            
            # Opens a new file and copies the reversed content of the original file into it.
            with open("__tempFile__", "w") as fileHandler2:
                [fileHandler2.write(line[::-1]) for line in fileContent]

                rename("__tempFile__", argv[1])

                print(f"\nThe content of {argv[1]} has been reversed successfully!")
    except Exception as exception:
        print(exception.__str__())


if __name__ == "__main__":
    main()
