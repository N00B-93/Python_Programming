from random import randint

"""
    This is a program that prompts the user to enter the length of a
    square matrix, randomly fills in 0s and 1s into the matrix, prints the matrix, and
    finds the rows, columns, and major diagonal with all 0's or all 1's.
"""


def checkColumnsWithOnes(matrix):
    flag = True
    columnsWithOnes = []

    for col in range(len(matrix)):
        for row in range(len(matrix[0])):
            if matrix[row][col] == 1:
                continue
            else:
                flag = False
        if flag:
            columnsWithOnes.append(col)
    return columnsWithOnes


def checkRowsForOnes(matrix):
    """
    Returns a list containing all rows that contains only 1's.

    :param matrix: (list) The matrix to be checked.

    :return: (list) The list of rows that contains only 1's.
    """
    flag = True
    rowsWithOnes = []

    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 1:
                continue
            else:
                flag = False
        if flag:
            rowsWithOnes.append(row)
    return rowsWithOnes


def main():
    # Prompts the user to enter the size of the square matrix.
    size = int(input("\nEnter the size of the square matrix: "))

    # Creates an empty list representing a matrix.
    matrix = []

    # Fills the matrix with 1's and 0's.
    for row in range(size):
        lst = []
        for column in range(size):
            lst.append(randint(0, 1))
        matrix.append(lst)

    rowsWithOnes = checkRowsForOnes(matrix)
    columnsWithOnes = checkColumnsWithOnes(matrix)

    print(rowsWithOnes, columnsWithOnes, matrix)


if __name__ == "__main__":
    main()
