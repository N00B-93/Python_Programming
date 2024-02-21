from random import randint

"""
    The Lo Shu Magic Square is a grid with 3 rows and 3 columns.
    Lo Shu Magic Square has the following properties:
    • The grid contains the numbers 1 through 9 exactly.
    • The sum of each row, each column, and each diagonal all add up to the same number.    This is a program that uses a function that accepts a 2-D list as an argument to determine if the list is a Lo Shu magic square or not.
"""


def sumOfRowElements(magicSquare, row):
    """
    Returns the sum of elements in a particular row of a matrix(2-D list).

    :param magicSquare: (list) The list whose sum of a given row is needed.

    :param row: (int) The index of the row whose sum of elements is to be determined.

    :return: (int) The sum of elements in the given row.
    """
    total = 0
    for column in range(len(magicSquare)):
        total += magicSquare[row][column]
    return total


def sumColumnElwments(magicSquare, column):
    """
    Returns the sum of elements in a particular column of a matrix(2-D list).
    
    :param magicSquare: (list) The list whose sum of a given column is needed.

    :param column: (int) The index of the column whose sum of elements is to be determined.

    :return: (int) The sum of elements in the given column.
    """
    total = 0
    for row in range(len(magicSquare)):
        total += magicSquare[row][column]
    return column


def sumMajorDiagonalElement(magicSquare):
    """
    Returns the sum of elements in a 3x3 matrix.

    :param magicSquare: (list) The 2-D matrix whose sum of element on it's major diagonal is to be determined.

    :return: (int) The sum of elements on the major diagonal.
    """
    total = 0
    for row in range(len(magicSquare)):
        for column in range(len(magicSquare)):
            if row == column:
                total += magicSquare[row][column]
    return total


def sumMinorDiagonal(magicSquare):
    """
    Returns the sum of elements on the minor digonal of a matrix(2-D list).

    :param magicSquare: (list) The matrix whose sum of minor diagonal is required.

    :return: (int) Sum of elements in the matrix(2-D list).
    """
    i, j, total = 2, 0, 0

    while i >= 0 and j <= 2:
        total += matrix[i][j]
        i -= 1
        j += 1
    return total



