from sys import exit

"""
    This is a program that uses a function with the header;
                def sortColumns(matrix)
    to sort the columns in a 3x3 matrix entered by the user.
"""


def sortColumns(matrix):
    """
    Sorts the columns in a 3x3 matrix.

    :param matrix: (list) The matrix whose columns is to be sorted.

    :return: None.
    """
    for passes in range(len(matrix)):
        for col in range(len(matrix[0])):
            for row in range(1, len(matrix)):
                if matrix[row][col] < matrix[row - 1][col]:
                    matrix[row][col], matrix[row - 1][col] = matrix[row - 1][col], matrix[row][col]


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
    print("\nMatrix before column sorting.")
    [[print(f"{matrix[row][col]} ", end="") for col in range(len(matrix[0]))]
        and print() for row in range(len(matrix))]

    # Sorts the columns of the matrix.
    sortColumns(matrix)

    # Displays the matrix after sorting.
    print("\nMatrix after column sorting.")
    [[print(f"{matrix[row][col]} ", end="") for col in range(len(matrix[0]))]
        and print() for row in range(len(matrix))]


if __name__ == "__main__":
    main()
