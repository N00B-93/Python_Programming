from random import randint

"""
    This is a program that displays an n x n matrix of 0's and 1's using the function
    with the header;
                def printMatrix(n):
"""


def printMatrix(n):
    """
    Displays an n x n matrix of 0's and 1's.

    :param n: (int) The number of rows in the square matrix.

    :return: None.
    """

    for i in range(n):
        for j in range(n):
            print(f"{randint(0, 1)} ", end="")
        print()
    return


def main():
    rows = int(input("\nEnter the number of rows: "))

    printMatrix(rows)


if __name__ == "__main__":
    main()
