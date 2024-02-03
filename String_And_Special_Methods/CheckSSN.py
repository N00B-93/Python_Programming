from sys import exit

"""
    This is a program that prompts the user to enter a Social Security
    number in the format ddd-dd-dddd, where d is a digit. The program displays
    Valid SSN for a correct Social Security number or Invalid SSN otherwise.
"""


def main():
    # Reads in an SSN Number.
    ssnNumber = input("\nEnter a Social Security Number(ddd-dd-dddd): ")

    # Displays an error message and terminates the program if the length of the SSN Number is not 11.
    if len(ssnNumber) != 11:
        print("Invalid SSN number!")
        exit(1)

    # Breaks the SSN Number into three sub strings.
    string1 = ssnNumber[0:3]
    string2 = ssnNumber[4:6]
    string3 = ssnNumber[7:11]

    # Checks if the sub strings are numeric strings and if the delimiters are equal to "-". Then displays if the SSN
    # Number is valid or not.
    if string1.isnumeric() and string2.isnumeric() and string3.isnumeric():
        if ssnNumber[3] == ssnNumber[6] == "-":
            print("\nValid SSN Number!")
        else:
            print("\nInvalid SSN Number!")
    else:
        print("\nInvalid SSN Number!")


if __name__ == "__main__":
    main()
