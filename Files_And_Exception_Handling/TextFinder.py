from sys import argv

"""
    This is a program that searches all files specified on the command line and 
    prints out all lines containing a specified word. The specified word is always the first command line argument. 
"""


def main() -> None:
    # checks if the user uses valid command line arguments.
    if len(argv) < 3:
        print("\nUsage: TextFinder.py textToFind FileToSearch1 FileToSearch2 FileToSearch3 ...")
        exit(1)

    # List to hold all occurrence of the word in the files.
    textAndFilename: list = []

    try:
        for i in range(2, len(argv)):  # Loops through the files to search for the occurrence of the specified word.
            with open(argv[i]) as fileHandler:
                for line in fileHandler:
                    if line.__contains__(argv[1]):  # Appends a line of text to the textAndFilename list if it contains
                        # the specified word.
                        textAndFilename.append(fileHandler.name + ": " + line.strip())
    except Exception as exception:
        print(exception.__str__())

    # Displays all occurrence of the word in the files.
    print()
    for item in textAndFilename:
        print(item)


if __name__ == "__main__":
    main()
