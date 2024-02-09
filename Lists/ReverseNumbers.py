"""
    This is a program that prompts the user to enter a list of numbers and
    displays the numbers in the reverse order in which they are entered.
"""


def main():
    # Reads in a list of numbers as a String.
    numberString = input("\nEnter a list of numbers separated by space: ")

    # Converts the String of numbers into a list of numbers
    numbers = numberString.split()

    # Displays the numbers in reverse order.
    print("\nThe numbers in reverse order are: ", end="")
    for i in range(len(numbers) - 1, -1, -1):
        print(f"{numbers[i]} ", end="")


if __name__ == "__main__":
    main()
