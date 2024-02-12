"""
    This is a program that uses a function with the header;
                def isConsecutiveFour(values)
    to check whether a list contains four consecutive numbers with the same values.
"""


def isConsecutiveFour(number, idx, numberList):
    """
    Checks if a list contains four consecutive numbers with the same values.

    :param number: (int) The number to be checked.

    :param idx: (int) The index of the number to be checked.

    :param numberList: (list) The list containing the number.

    :return: (bool) True if the number is consecutive four and False otherwise.
    """
    counter = 0
    for i in range(idx, idx + 4):
        if number == numberList[i]:
            counter += 1
    return counter == 4


def main():
    # reads in a list of numbers as a String.
    numberString = input("\nEnter a list of numbers separated by a space: ")

    # Converts the String of numbers to a list.
    numberList = numberString.split()

    # Converts the elements of the list into int.
    numberList = list(map(int, numberList))

    check, consecutiveFour = 0, False

    # Checks if each digit in the list is a consecutive four digit.
    for i in range(len(numberList) - 3):
        check = isConsecutiveFour(numberList[i], i, numberList)
        if check:
            consecutiveFour = True
            break
    # Displays the result.
    if consecutiveFour:
        print("\nThe list has consecutive four")
    else:
        print("\nThe does not have consecutive four")


if __name__ == "__main__":
    main()
