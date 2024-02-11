"""
    This is a program that prompts the user to enter a list of numbers
    and uses a function with the header;
                def isSorted(lst)
    to determine whether the list is sorted in ascending order or not.
"""


def isSorted(lst):
    """
    Checks if the list is sorted in ascending order or not.

    :param lst: (list) List of numbers to be checked.

    :return: (bool) True if list is sorted in ascending order else False.
    """
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False
    return True


def main():
    # Reads in a list of numbers as a String.
    numberString = input("\nEnter a list of numbers separated by space: ")

    # Converts the String of numbers to a list.
    numberList = numberString.split()

    # Converts each element in numberList to integers or float.
    numberList = [eval(numberList[i]) for i in range(0, len(numberList))]

    # Displays the result.
    if isSorted(numberList):
        print("\nThe list is already sorted.")
    else:
        print("\nThe list is not sorted.")


if __name__ == "__main__":
    main()
