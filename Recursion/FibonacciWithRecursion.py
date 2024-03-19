"""
    This is a program that prompts the user to enter an index and then displays the fibonacci number that
    corresponds to that index using recursion.
"""

# Initializes a variable to count the number of recursive calls made.
countRecursiveCalls = 0


def fibonacciWithRecursion(index):
    """
    This returns the Fibonacci number at a particular index using recursion.
    :param index: (int) The index of the Fibonacci number
    :return: (int) The Fibonacci number at the given index.
    """
    global countRecursiveCalls
    countRecursiveCalls += 1
    if index == 0:
        return 0
    elif index == 1:
        return 1
    else:
        return fibonacciWithRecursion(index - 1) + fibonacciWithRecursion(index - 2)


def main() -> None:
    while True:
        try:
            # Prompts the user to enter the index of the Fibonacci number to be displayed.
            number: int = int(input("\nEnter an index > 0 for a Fibonacci number: "))

            # Displays the Fibonacci number at the index supplied by the user and the number of recursive calls.
            print(f"\nThe Fibonacci number at index {number} is: {fibonacciWithRecursion(number)}")
            print(f"\nNumber of recursive calls: {countRecursiveCalls}")
            break
        except ValueError:
            print("\nInvalid input. Try again.")


if __name__ == "__main__":
    main()
