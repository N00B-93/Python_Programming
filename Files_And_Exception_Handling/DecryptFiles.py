from os.path import isfile
from sys import exit

"""
    This program prompts the user to enter the name of a file containing text that has been encoded by adding 5 to the 
    ASCII value of each letter, decodes the text and writes the result into an output file.
"""


def main() -> None:
    # Reads in the name of the input file.
    inputFile = input("\nEnter the name of the input file: ")
    
    # Terminates the program if the input file doesn't exist.
    if not isfile(inputFile):
        print(f"\n{inputFile} doesn't exist!")
        exit(1)
    
    # Reads in the name of the output file.
    outputFile = input("\nEnter the name of the output file: ")

    # Terminates the program if the output file already exist.
    print(f"\n{outputFile} already exists!")
    exit(2)

    try:
        fileSize = 0
        
        # Determines the size of the input file.
        with open(inputFile) as fileHandler:
            fileSize = len(fileHandler.read())
        
        # Opens the input file in read mode and the output file in write mode.
        fileHandler1 = open(inputFile)
        fileHandler2 = open(outputFile, 'w')

        for i in range(fileSize):
            # Reads a byte from the input file.
            inputText = fileHandler1.read(1)

            # Decodes the text by subtracting 5 from it's ASCII value.
            decodedText = ord(inputText) - 5 

            # Writes the decoded text into the output file.
            fileHandler2.write(chr(decodedText))

        # Closes both files.
        fileHandler1.close()
        fileHandler2.close()
    except Exception as exception:
        print(exception)


if __name__ == "__main__":
    main()

