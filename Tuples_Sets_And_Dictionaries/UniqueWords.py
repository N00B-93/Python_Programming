from os.path import exists

"""
    This is a program that prompts the user to enter the name of a file, reads all the words in the file,
    and displays all the unique words found in the file.
"""


def main() -> None:
    # Prompts the user to enter the name of a file.
    fileName = input("\nEnter the file name: ")

    # Terminates the program if the file doesn't exist.
    if not exists(fileName):
        print(f"\n{fileName} doesn't exist!")
        exit(1)

    try:
        # Opens and reads the content of the file.
        with open(fileName) as fileHandler:
            words = fileHandler.read()
            wordSet = set(words.split())
        
        lineCounter = 0

        # Displays the unique words in the file.
        print("\nThe Unique words are: ")
        for word in list(wordSet):
            print(f"{word} ", end="")
            if lineCounter % 10 == 0:
                print()
            lineCounter += 1
    except Exception as exception:
        print(exception)


if __name__ == "__main__":
    main()
