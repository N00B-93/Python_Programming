from sys import exit

"""
    This is a program that prompts the user to enter a number n and displays the pattern;
                        1
                      2 1
                    3 2 1
            ...
          n n-1 ... 3 2 1
    using a function with the header;
            def displayPattern(n)
"""


def displayPattern(n):
    """
    Displays the pattern;

                        1
                      2 1
                    3 2 1
            ...
          n n-1 ... 3 2 1
    in the console.

    :param n: (int) The number of rows in the triangular shape.

    :return: None
    """
    space = n

    m = 1

    for i in range(0, n):
        for j in range(space):
            print("  ", end="")

        for k in range(m, 0, -1):
            print(f"{k} ", end="")
        space -= 1
        m += 1
        print()


def main():
    # Reads in a positive number.
    number = int(input("\nEnter a  positive integer: "))

    # Prints an error message and terminates the program if the number entered is negative.
    if number < 0:
        print("\nPositive number required, Try again.")
        exit(1)

    # Displays the pattern.
    displayPattern(number)


if __name__ == "__main__":
    main()
