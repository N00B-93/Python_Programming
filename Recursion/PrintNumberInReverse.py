"""
    This is a program that prompts the user to enter an integer and then uses a method with the header:
                def reverseDisplay(number)
    to display the number in reverse order.
"""


def reverseDisplay(number: int) -> None:
    """
    This function displays an integer in reverse using recursion.

    :param number: (int) The integer to be displayed in reverse order.

    :return: None
    """
    if number > 0:
        remainder: int = number % 10
        print(f"{remainder}", end="")
        reverseDisplay(number // 10)


def main() -> None:
    while True:
        try:
            # Prompts the user to enter an integer to be displayed in reverse.
            number = int(input("\nEnter an Integer: "))

            # Displays the number in reverse.
            print(f"\n{number} in reverse is: ", end="")
            reverseDisplay(number)
            print()
            break
        except ValueError:
            print("\nInvalid input, Try again.")


if __name__ == "__main__":
    main()
