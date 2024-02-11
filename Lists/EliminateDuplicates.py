"""
    This is a function that prompts the user to enter a list of numbers and then
    remove the duplicates in the list using a function with the header;
                def eliminateDuplicates(lst):
"""


def eliminateDuplicates(lst):
    """
    Returns a list of distinct elements from a given list.

    :param lst: (list) The given list.

    :return: (list) The list of distinct elements from the given list.
    """
    distinctElements = []
    for i in range(len(lst)):
        if lst[i] not in distinctElements:
            distinctElements.append(lst[i])
    return distinctElements


def main():
    # Reads in a list of numbers as a String.
    numberString = input("\nEnter enter a list of numbers separated by space: ")

    # Converts the list of numbers to a list.
    numberList = numberString.split()

    # Converts each element of the numberList to integers or floats
    numberList = [eval(numberList[i]) for i in range(0, len(numberList))]

    # Determines the distinct elements.
    distinctElements = eliminateDuplicates(numberList)

    # displays the distinct elements.
    print("\nThe list of distinct elements is: ", end="")
    [print(f"{distinctElements[i]} ", end="") or i for i in range(len(distinctElements))]


if __name__ == "__main__":
    main()
