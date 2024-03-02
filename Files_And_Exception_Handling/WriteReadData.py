from random import randint
from os.path import isfile
from sys import exit

"""
    This is a program that writes 100 integers created randomly into a file. Integers are separated by a space 
    in the file. The program then reads the numbers out of the file, sorts them and displays them.
"""


def main() -> None:
    # Prompts the user to enter the name of the file to save the generated numbers in.
    nameOfFile = input("\nEnter the name of the file to write numbers to: ")

    # Terminates the program if the file already exists.
    if isfile(nameOfFile):
        print("\nThe file already exists!\nTry again with a different file name.")
        exit(1)

    try:
        # Creates a file and opens it in write mode.
        with open("numbers.txt", 'w') as fileHandler:
            # Writes 100 integers from 1 to 1000 separated by space into the numbers.txt file.
            for i in range(100):
                fileHandler.write(str(randint(1, 1000)) + " ")
        print("\n100 Random numbers written to file!")

        # Reads the integers written into the file.
        with open('numbers.txt') as fileHandler:
            numberString = fileHandler.read()
            listOfNumbers = numberString.split()
            listOfNumbers = [int(listOfNumbers[i]) for i in range(len(listOfNumbers))]

            # Sorts the list of numbers read from the file.
            listOfNumbers.sort()

            # Displays the sorted list.
            print("\nThe sorted list of numbers is: ", end="")
            [print(f"{listOfNumbers[i]} ", end="") or i for i in range(len(listOfNumbers))]
            print()
    except Exception as exception:
        print(exception)


if __name__ == "__main__":
    main()
