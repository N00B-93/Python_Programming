"""
    This is a program that prompts the user to enter a series of  integers
    and displays all the combinations of picking two numbers from the number of integers entered.
"""


def main():
    # Reads in a series of numbers as a String.
    numberString = input("\nEnter a list of integers separated by space: ")

    # Converts the String of numbers to a list.
    numberList = numberString.split()

    # Converts all the elements of the number list to integers.
    numberList = list(map(int, numberList))

    # Displays all possible combination of picking two numbers.
    print(f"\nAll combination of picking two numbers from {len(numberList)} are: ", end="")
    for i in range(len(numberList)):
        for j in range(i + 1, len(numberList)):
            print(f"{(numberList[i], numberList[j])} ", end="")
    print()


if __name__ == "__main__":
    main()
