"""
    This is a program that prompts the user to enter an index and then displays the fibonacci number that
    corresponds to that index.
"""


def fibonacciWithoutRecursion(index: int) -> int:
    """
    This returns the Fibonacci number at a particular index.
    :param index: (int) The index of the Fibonacci number
    :return: (int) The Fibonacci number at the given index.
    """
    previous = 0
    current = 1

    for i in range(2, index + 1):
        nextTerm = previous + current
        previous = current
        current = nextTerm
    return current


def main() -> None:
    while True:
        try:
            # Prompts the user to enter the index of the Fibonacci number to be displayed.
            number: int = int(input("\nEnter an index > 0 for a Fibonacci number: "))

            # Displays 0 if index entered by user is 0.
            if number == 0:
                print(f"\nThe Fibonacci number at index {number} is: 0")
                break
            # Displays 1 if index entered by user is 1.
            elif number == 1:
                print(f"\nThe Fibonacci number at index {number} is: 1")
                break
            else:
                # Displays the Fibonacci number at the index supplied by the user.
                print(f"\nThe Fibonacci number at index {number} is: {fibonacciWithoutRecursion(number)}")
                break
        except ValueError:
            print("\nInvalid input. Try again.")


if __name__ == "__main__":
    main()
