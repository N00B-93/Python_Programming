from math import pow, sqrt

"""
    This is a program that prompts the user to enter a list of numbers and displays the
    mean and standard deviation using two functions with headers;
                def deviation(x):
            and
                def mean(x):
"""


def mean(lst):
    """
    Returns the mean of a list of numbers.

    :param lst: (list) A list of numbers whose mean is to be determined.

    :return: (float) The mean of the list of numbers.
    """
    return sum(lst) / len(lst)


def deviation(lst):
    """
    Return the standard deviation of a list of numbers.

    :param lst: (list) The list of numbers.

    :return: (float) The standard deviation.
    """
    meanDeviation = 0

    for i in range(len(lst)):
        meanDeviation += pow(lst[i] - mean(lst), 2)

    return sqrt(meanDeviation / (len(lst) - 1))


def main():
    # Reads in a String of numbers.
    numberString = input("\nEnter a list of numbers separated by space: ")
    
    # Converts thw String of numbers to a list.
    numberList = numberString.split()
    
    # Converts the elements in the list to integers.
    numberList = [eval(numberList[i]) for i in range(len(numberList))]
    
    # Displays the result.
    print(f"\nMean = {mean(numberList):.2f}\nStandard Deviation = {deviation(numberList):.2f}")


if __name__ == "__main__":
    main()
