from random import randint
from sys import exit

"""
    The Lo Shu Magic Square is a grid with 3 rows and 3 columns.
    Lo Shu Magic Square has the following properties:
    • The grid contains the numbers 1 through 9 exactly.
    • The sum of each row, each column, and each diagonal all add up to the same number.
    This is a program that uses a function that accepts a 2-D list as an argument to determine 
    if the list is a Lo Shu magic square or not.
"""


def sumOfRowElements(magicSquare, row):
    """
    Returns the sum of elements in a particular row of a matrix(2-D list).

    :param magicSquare: (list) The list whose sum of a given row is needed.

    :param row: (int) The index of the row whose sum of elements is to be determined.

    :return: (int) The sum of elements in the given row.
    """
    return sum(magicSquare[row])


def sumOfColumnElements(magicSquare, column):
    """
    Returns the sum of elements in a particular column of a matrix(2-D list).
    
    :param magicSquare: (list) The list whose sum of a given column is needed.

    :param column: (int) The index of the column whose sum of elements is to be determined.

    :return: (int) The sum of elements in the given column.
    """
    total = 0
    for row in range(len(magicSquare)):
        total += magicSquare[row][column]
    return total


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


def sumMinorDiagonalElement(magicSquare):
    """
    Returns the sum of elements on the minor diagonal of a matrix(2-D list).

    :param magicSquare: (list) The matrix whose sum of minor diagonal is required.

    :return: (int) Sum of elements in the matrix(2-D list).
    """
    i, j, total = len(magicSquare) - 1, 0, 0

    while i >= 0 and j <= len(magicSquare) - 1:
        total += magicSquare[i][j]
        i -= 1
        j += 1
    return total


def checkLoShuMatrix(magicSquare):
    """
    Returns True if a matrix is a Lo Shu matrix, else returns False.

    :param magicSquare: (list) The matrix to be checked.

    :return: (bool) True if the matrix is a Lo shu matrix, else False.
    """
    check, flag = [], True

    for i in range(len(magicSquare)):
        check.append(sumOfRowElements(magicSquare, i))

        check.append(sumOfColumnElements(magicSquare, i))
    
    check.append(sumMajorDiagonalElement(magicSquare))
    check.append(sumMinorDiagonalElement(magicSquare))

    for i in range(1, len(magicSquare)):
        if check[i] == check[0]:
            continue
        else:
            flag = False
            break
    return flag


def main():
    # Creates an empty list to hold the matrix.
    magicSquare = []

    # Reads in the dimension of a square matrix.
    row = int(input("\nEnter the number of row of the square matrix: "))
    column = int(input("\nEnter the number of columns of the square matrix: "))
    
    print()

    # Terminates the program if the row is not equal to the column.
    if row != column:
        print("\nRow must be equal to column!")
        exit(1)
    
    # Populates the magicSquare with number numbers from 0 to 9.
    for i in range(row):
        lst = []
        for j in range(column):
            lst.append(randint(1, 9))
        magicSquare.append(lst)

    # Displays the generated matrix.
    for i in range(row):
        for j in range(column):
            print(f"{magicSquare[i][j]} ", end="")
        print()
    
    # Checks if the matrix is a Lo Shu matrix.
    flag = checkLoShuMatrix(magicSquare)
    if flag:
        print("\nThe matrix is a Lo Shu matrix.")
    else:
        print("\nThe matrix is not a Lo Shu matrix.")

    
if __name__ == "__main__":
    main()
