"""
    This is a program that uses a function with the header;
            def indexOfSmallestElement(lst):
    to determine the index of the smallest element in a list. The first index is returned if the number occurs more
    than once.
"""


def indexOfSmallestElement(lst):
    """
    Returns the index of the smallest element in a list of numbers. If the element appears more 
    than once, the index of the first occurrence is returned.

    :param lst: (list) The list of numbers.

    :return: (int) Index of smallest element in the list.
    """
    return lst.index(min(lst))


def main():
    # Reads in a collection of numbers as a String.
    numberString = input("\nEnter a list of integers separated by space: ")
    
    # Converts the number String to a list.
    numberList = numberString.split()
    
    # Converts every element of the number list to integers.
    map(int, numberList)
    
    # Displays the result.
    print(f"\nThe index of the smallest element is: {indexOfSmallestElement(numberList)}")


if __name__ == "__main__":
    main()
