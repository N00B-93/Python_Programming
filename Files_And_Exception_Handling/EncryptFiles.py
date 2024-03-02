from os.path import isfile
from sys import exit

"""
    This program prompts the user to enter the name of the input file and output file, reads each byte from
    the input file and encode it by adding 5 to it's ASCII value. The result is then written into the output file.
"""


def main() -> None:
    # Reads in the input file name.
    inputFile = input("\nEnter input file name: ")
    
    # Terminates the program if the input file doesn't exist.
    if not isfile(inputFile):
        print(f"\n{inputFile} doesn't exist!")
        exit(1)

    # Reads in the output file name.
    outputFile = input("\nEnter output file name: ")
    
    # Terminates the program if the output file already exists.
    if isfile(outputFile):
        print(f"\n{outputFile} already exists!")
        exit(2)
    
    try:
        # Determines the size of the input file.
        with open(inputFile) as fileHandler:
            fileContent = fileHandler.read()
            fileSize = len(fileContent)
        
        # Opens input file in read mode and output file in write mode.
        fileHandler1 = open(inputFile)
        fileHandler2 = open(outputFile, 'w')

        for i in range(fileSize):
            # Reads a byte of data from the input file.
            inputText = fileHandler1.read(1)

            # Encode the byte by adding 5 to it's ASCII value.
            encodedText = ord(inputText) + 5

            # Writes the encoded byte into the output file.
            fileHandler2.write(chr(encodedText))
        print(f"\nText encoded and output written to {outputFile}!")

        # Closes the input and output files.
        fileHandler1.close()
        fileHandler2.close()

    except Exception as exception:
        print(exception)


if __name__ == "__main__":
    main()
