"""
    This is a program that prompts the user to enter the name of a file and then displays the number of words,
    letters and lines in  the file.
"""


def countWords(fileName):
    """
    Returns the number of words in a text file.

    :param fileName: (str) The name of the text file.

    :return: (int) Number of words in the file.
    """
    words = []
    try:
        with open(fileName, 'r') as fileHandler:
            words = (fileHandler.read()).split()
    except IOError as ioError:
        raise ioError
    except Exception as exception:
        raise exception
    return len(words)


def countCharactersAndLines(fileName):
    """
    Returns the number of lines and characters in a text file.

    :param fileName: (str) The name of the text file.

    :return: (int), (int) The number of lines and characters in the text file.
    """
    characters = lines = 0
    try:
        with open(fileName, 'r') as fileHandler:
            for line in fileHandler:
                characters += len(line)
                lines += 1
    except IOError as ioError:
        raise ioError
    except Exception as exception:
        raise exception
    return lines, characters


def main() -> None:
    # Prompts the user to enter the name of the file.
    fileName = input("\nEnter the name of the file: ")
    try:

        # Determines the number of Words, Characters and Lines.
        words = countWords(fileName)
        lines, characters = countCharactersAndLines(fileName)
        # Prints the number of Characters, Words and Lines.
        print("\nThe file contains: ")
        print(f"\n{characters} chatacters")
        print(f"\n{words} words")
        print(f"\n{lines} lines")
    except Exception as exception:
        print(exception)


if __name__ == "__main__":
    main()

