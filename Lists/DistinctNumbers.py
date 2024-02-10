"""
    This is a program that reads in numbers separated by a
    space in one line and displays distinct numbers (i.e., if a number appears multiple
    times, it is displayed only once).
"""


def main():
    # Reads in a String of numbers.
    numberString = input("\nEnter a list of numbers separated by a space: ")

    # Converts the String of numbers into a list.
    numberList = numberString.split()

    # Creates an empty list to hold distinct numbers.
    distinctNumbersList = []

    # Appends only one instance of each number in the distinct numbers list.
    for number in numberList:
        if number not in distinctNumbersList:
            distinctNumbersList.append(number)

    # Sorts the distinct numbers.
    distinctNumbersList.sort()

    # Displays the distinct numbers.
    print(f"\nThe distinct numbers are: ", end="")
    for number in distinctNumbersList:
        print(f"{number} ", end="")


if __name__ == "__main__":
    main()
