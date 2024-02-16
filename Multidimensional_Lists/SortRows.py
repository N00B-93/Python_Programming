from sys import exit

"""
    This is a program that uses a function with the header;
                def sortRows(matrix)
    to sort the rows in a 3x3 matrix entered by the user.
"""


def sortRows(matrix):
    """
    Sorts the rows in a 3x3 matrix.

    :param matrix: (list) The matrix whose row is to be sorted.

    :return: None.
    """
    [matrix[row].sort() for row in range(len(matrix))]


def main():
    matrix = []

    # Reads in the element of the matrix.
    for row in range(3):
        line = input(f"\nEnter element of row {row} separated by space: ").strip().split()
        # terminates the program if the number of elements in a row is not equal to the number of columns.
        if len(line) != 3:
            print("\nUse 3 elements in a row!")
            exit(1)
        matrix.append([eval(x) for x in line])

    # Displays the matrix before sorting.
    print("\nMatrix before row sorting.")
    [[print(f"{matrix[row][col]} ", end="") for col in range(len(matrix[0]))]
     and print() for row in range(len(matrix))]

    # Sorts the rows of the matrix.
    sortRows(matrix)

    # Displays the matrix after sorting.
    print("\nMatrix after row sorting.")
    [[print(f"{matrix[row][col]} ", end="") for col in range(len(matrix[0]))]
     and print() for row in range(len(matrix))]


if __name__ == "__main__":
    main()
