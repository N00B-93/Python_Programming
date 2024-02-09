"""
    This is a program that prompts the user to enter a list of numbers and reverses the
    list using a function with the heeader;
            def reverseList(lst)
"""


def reverseList(lst):
    """
    Returns a list in reverse.

    :param lst: (list) The list to be reversed.

    :return: (list) The reverse of the list.
    """
    return lst[::-1]


def main():
    # Reads in a list of numbers as a String.s
    numberString = input("\nEnter a list of numbers: ")

    # Converts the String of numbers into a list.
    numberList = numberString.split()
    
    # Reverses the list.
    reversedList = reverseList(numberList)

    # Displays the result.
    print("\nThe reversed list is: ", end="")
    for i in range(len(reversedList)):
        print(f"{reversedList[i]} ", end="")
    print()


if __name__ == "__main__":
    main()

