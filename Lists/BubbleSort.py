"""
    The bubble-sort algorithm makes several passes through the list. On each pass,
    successive neighboring pairs are compared. If a pair is in decreasing order,
    its values are swapped; otherwise, the values remain unchanged. The technique is called a bubble sort or
    sinking sort because the smaller values gradually “bubble” their way to the top and the larger values “sink” to
    the bottom.
    This is a program that uses a function with the header;
                def bubbleSort(lst)
    to sort a list of numbers entered by the user in ascending order.
"""


def bubbleSort(lst):
    """
    Sorts a list using the Bubble Sort Algorithm.

    :param lst: (list) The list to be sorted.

    :return: None.
    """
    for i in range(len(lst)):
        for j in range(1, len(lst)):
            if lst[j] < lst[j - 1]:
                lst[j - 1], lst[j] = lst[j], lst[j - 1]


def main():
    # Reads in a collection of numbers as a String
    numberString = input("\nEnter a list of numbers separated by space: ")
    
    # Converts the string of numbers to a list.
    numberList = numberString.split()
    
    # Converts all elements in the number list to integers.
    numberList = [eval(numberList[i]) for i in range(len(numberList))]
    
    # Sorts the list.
    bubbleSort(numberList)
    
    # Displays the sorted list in ascending order.
    print("\nThe sorted list is: ", end="")
    [print(f"{numberList[i]} ", end="") or i for i in range(len(numberList))]


if __name__ == "__main__":
    main()
