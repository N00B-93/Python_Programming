from os.path import exists

"""
    This is a program that prompts the user to enter the name of a file and then displays the first 5 lines of
    the file. If the file contains less than 5 lines, the whole file content is displayed.
"""


def main() -> None:
    # Prompts the user to enter the name of a file to read from.
    fileName: str = input("\nEnter a filename: ")

    # Continues to prompt the user to enter a valid filename if the name entered by the user doesn't exist.
    while not exists(fileName):
        print(f"\n{fileName} doesn't exist, Use a valid filename.")
        fileName = input("\nEnter a filename: ")

    # Opens the file and reads and displays the first 5 lines.
    with open(fileName) as fileHandler:
        firstFiveLines = fileHandler.readlines()

        if len(firstFiveLines) > 5:
            print(f"\nThe first 5 lines of {fileName} is: ")
            [print(firstFiveLines[i]) or i for i in range(5)]
        else:
            print(f"\nThe first {len(firstFiveLines)} lines of {fileName} is: ")
            [print(line) or 1 for line in firstFiveLines]


if __name__ == "__main__":
    main()
