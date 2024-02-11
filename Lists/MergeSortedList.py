from sys import exit
from SortedList import isSorted

"""
    This is a program that prompts the user to enter two list already sorted in ascending order,
    then merge them into a single list and displays the merged list sorted in ascending order.
"""


def mergeSortedList(lst1, lst2):
    """
    Merge two lists into a single list and return the merged list sorted in ascending order.

    :param lst1: (list) The first list.

    :param lst2: (list) The second list.

    :return: (list) The merged list sorted in ascending order.
    """
    return sorted(lst1 + lst2)


def main():
    # Reads in two lists of numbers as Strings.
    nuberString1 = input("\nEnter the first list of numbers separated by space: ")
    nuberString2 = input("\nEnter the second list of numbers separated by space: ")

    # Converts the String of numbers to lists.
    numberList1 = nuberString1.split()
    numberList2 = nuberString2.split()

    # Converts each element in the number list to integers or float.
    numberList1 = [eval(numberList1[i]) for i in range(len(numberList1))]
    numberList2 = [eval(numberList2[i]) for i in range(len(numberList2))]

    if not isSorted(numberList1) or not isSorted(numberList2):
        print("\nUse sorted lists!")
        exit(1)

    # Mergers the two lists and sorts the result.
    numberList3 = mergeSortedList(numberList1, numberList2)

    # Displays the sorted merged list.
    print("\nThe Merged list is: ", end="")
    for i in range(len(numberList3)):
        print(f"{numberList3[i]} ", end="")


if __name__ == "__main__":
    main()
