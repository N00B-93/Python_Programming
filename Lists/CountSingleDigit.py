from random import randint


"""
    This is a program that generates 1,000 random integers
    between 0 and 9 and displays the count for each number.
"""


def countOccurrence(number, numbers):
    """
    This function returns the number of occurrences of a number in a list of numbers.

    :param number: (int) The number to be counted.

    :param numbers: (list) The list of numbers.

    :return: (int) The number of occurrences of the number.
    """
    return numbers.count(number)


def main():
    # Creates a list.
    numbers = []

    # Append 100 integers in the range 0 to 9 to the list.
    for i in range(1000):
        numbers.insert(i, randint(0, 9))

    # Displays each numbers and it's frequency of occurrence.
    print("\nNumber\t\tNumber of Occurrences")
    for i in range(10):
        print(f"{i}\t\t{countOccurrence(i, numbers):21}")


if __name__ == "__main__":
    main()
