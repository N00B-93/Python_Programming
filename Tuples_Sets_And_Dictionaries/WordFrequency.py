from os.path import exists

"""
    This is a program that prompts the user to enter the name of a file, reads all the words from the file,
    then displays each word and its number of occurrence in the file.
"""


def main() -> None:
    # Reads in a file name.
    fileName = input("\nEnter a file name: ")
    
    # Terminates the program if the file doesn't exist.
    if not exists(fileName):
        print(f"\n{fileName} doesn't exist!")
        exit(1)

    # Creates a list and a dictionary to store the words read from the file.
    words, wordsAndOccurrence = [], {}
    
    try:
        # Opens the file and reads all the words as a single string.
        with open(fileName) as fileHandler:
            # Tokenize the String read from the file.
            words = fileHandler.read().split()
    
        for word in words:
            # Continues the iteration if the current word exists as a key in the dictionary.
            if word in wordsAndOccurrence:
                continue
            else:
                # Append a word and its occurrence in the wordsAndOccurrence dictionary.
                wordsAndOccurrence.update({word: words.count(word)})
    
        # Displays each word and its occurrence.
        print("\nWord\t\t\tOccurrence")
        for key, value in wordsAndOccurrence.items():
            print(f"{key.ljust(33)}{value}")
    except IOError as ioError:
        print(ioError)
    except Exception as exception:
        print(exception)


if __name__ == "__main__":
    main()
