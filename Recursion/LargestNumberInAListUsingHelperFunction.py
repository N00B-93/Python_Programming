"""
    This is a program that prompts the user to enter a list of numbers and then displays the largest number
    in the list using a recursive function.
"""

# Global variable to reference the largest element in the list.
maxInteger = 0


def getLargestElementHelper(listOfNumbers: list, high: int) -> int:
    """
    Returns the largest element in the list by taking a list and the index of the last element in the list
    from another function.

    :param listOfNumbers: (list) The list of numbers.

    :param high: (int) The index of the last element in the list.

    :return: (int) The largest element in the list.
    """
    global maxInteger

    if high < 0:
        return maxInteger
    elif listOfNumbers[high] > maxInteger:
        maxInteger = listOfNumbers[high]
    return getLargestElementHelper(listOfNumbers, high - 1)


def getLargestElement(listOfNumbers: list) -> int:
    """
    Determines the largest element of a list using a recursive helper function.

    :param listOfNumbers: (list) A list of numbers whose largest element should be returned.

    :return: (int) The largest element of the list.
    """
    return getLargestElementHelper(listOfNumbers, len(listOfNumbers) - 1)


def main() -> None:
    # Prompts the user to enter a list of numbers.
    listOfNumbers: str = input("\nEnter a list of numbers separated by space: ")

    # Converts the list of numbers from String to list of Strings.
    listOfNumbers: list = listOfNumbers.split()

    # Converts every element of the listOfNumber list to integers.
    listOfNumbers: list = list(map(int, listOfNumbers))

    # Displays the largest element in the list.
    print(f"\nThe largest number in the list is: {getLargestElement(listOfNumbers)}")


if __name__ == "__main__":
    main()
