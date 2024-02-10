from random import randint


"""
    This is a program that prompts the user to enter a list of numbers and then shuffle
    the list using a function with the headee;
                def shuffle(lst)
    and then displays the shuffled list.
"""


def shuffle(lst):
    """
    Shuffles a given list.

    :param lst: (list) The list to be shuffled.

    :return: None.
    """
    previousIndex = ""

    for i in range(len(lst)):
        currentIndex = randint(0, len(lst) - 1)
        while currentIndex == previousIndex:
            currentIndex = randint(0, len(lst) - 1)
        lst[i], lst[currentIndex] = lst[currentIndex], lst[i]

        previousIndex = currentIndex


def main():
    # Reads in a collection of numbers as a String.
    numberString = input("\nEnter a list of numbers separated by space: ")
    
    # Converts the String of numbers to a list.
    numberList = numberString.split()
    
    # Shuffles the list
    shuffle(numberList)
    
    # Prints the shuffled list.
    print("\nThe shuffled list is: ", end="")
    for i in range(len(numberList)):
        print(f"{numberList[i]} ", end="")
    print()


if __name__ == "__main__":
     main()

