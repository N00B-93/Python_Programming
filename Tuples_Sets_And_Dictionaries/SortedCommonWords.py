from os.path import exists

"""
    This is a program that reads in the name of two files and then prints out in sorted order, all the 
    words that are common to the two files.
"""


def main() -> None:
    # Reads in the name or path of the first file.
    file1: str = input("\nEnter the name or path of the first file: ")

    # Displays an error message and terminates the program if the first file doesn't exist.
    if not exists(file1):
        print(f"\n{file1} doesn't exists!!!")
        exit(1)
    
    # Reads in the name or path of the second file.
    file2: str = input("\nEnter the name or path of the second file: ")

    # Displays an error message and terminates the program if the second file doesn't exist.
    if not exists(file2):
        print(f"\n{file2} doesn't exists!!!")
        exit(2)

    try:
        # Opens the first file and reads it's content.
        with open(file1) as fileHandler1:
            file1Content: set = set(fileHandler1.read().split())
        
        # Opens the first file and reads it's content.
        with open(file2) as fileHandler2:
            file2Content: set = set(fileHandler2.read().split())
        
        # Creates a set of words common to both files.
        generalUniqueWords: set = file1Content.intersection(file2Content)
        
        # Converts the set of common words to a list.
        generalUniqueWords: list = list(generalUniqueWords)
        
        # Sorts the list of common words.
        generalUniqueWords.sort()
        
        # Displays the result.
        print("The words common to both files are: ")
        for word in generalUniqueWords:
            print(f"{word} ")

    except Exception as exception:
        print(exception.__str__())


if __name__ == "__main__":
    main()
