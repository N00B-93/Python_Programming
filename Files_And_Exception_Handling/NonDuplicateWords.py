from os.path import isfile

"""
    This is a program that prompts the user to enter a text file, reads words from the file, and displays all the 
    non-duplicate words in ascending order.
"""


def main() -> None:
    # Prompts the user to enter the name of a file.
    fileName = input("\nEnter the name of the file: ")

    # Prints an error message and terminates the program if the filename entered by the user doesn't exist.
    if not isfile(fileName):
        print(f"\n{fileName} doesn't exist!!!")
        exit(1)

    # Creates a set Object to hold the unique words in the file.
    fileContent: set = set()

    with open(fileName) as fileHandler:
        # Reads out the content of the file as a String and converts it to a list.
        listOfWords: list = fileHandler.read().split()

        # Appends words from the file to the set Object.
        [fileContent.add(word) for word in listOfWords]

    # Returns a list of sorted words.
    sortedWords = sorted(fileContent)

    # Displays the unique words in the file.
    for word in sortedWords:
        print(word)


if __name__ == "__main__":
    main()
