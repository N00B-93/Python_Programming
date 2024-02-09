"""
    This is a program that reads some integers
    between 1 and 100 and counts the occurrences of each.
"""


def main():
    # Reads in a String of numbers
    numberString = input("\nEnter a list of integers between 1 and 100 separated by a space: ")

    # Converts the String of numbers into a list of Strings.
    numberList = numberString.split()

    # Changes each element of the number list from str to int.
    numberList = [int(numberList[i]) for i in range(len(numberList))]

    # Sorts the list of numbers.
    numberList.sort()

    # Creates a list to contain distinct element and their number of occurrence in numberList.
    distinctNumbers = []
    frequency = []

    # Appends only one instance of a number to the distinct element list and counts appends it's number of occurrence to
    # the frequency list.
    for element in numberList:
        if element not in distinctNumbers:
            distinctNumbers.append(element)
            frequency.append(numberList.count(element))

    # displays each number and it's frequency of occurrence.
    for i in range(len(distinctNumbers)):
        if frequency[i] > 1:
            print(f"\n{distinctNumbers[i]} occurs {frequency[i]} times")
        else:
            print(f"\n{distinctNumbers[i]} occurs {frequency[i]} time")


if __name__ == "__main__":
    main()
