"""
    A nxn matrix is called a positive Markov matrix if each element
    is positive and the sum of the elements in each column is 1.
    This is a program that prompts the user to enter the rows of a matrix and checks if the
    matrix is a valid Markov matrix or not.
"""


def checkSign(matrix):
    """
    Checks if the all elements of a matrix(list) are positive.

    :param matrix: (list) The matrix whose elements are to be checked.

    :return: (bool) True if the all elements are positive, false otherwise.
    """
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] < 0:
                return False
    return True


def checkSumOfColumns(matrix):
    """
    Returns True if the sum of each column in the matrix(list) is positive and False otherwise.

    :param matrix: (list) The matrix to be processed.

    :return: (bool) True if the sum of each column is positive, false otherwise.
    """
    for i in range(len(matrix)):
        total = 0
        for j in range(len(matrix[0])):
            total += matrix[j][i]
        if total != 1:
            return False
    return True


def main():
    # Creates an empty list to represent a matrix.
    matrix = []

    # Reads in the number of rows and columns of the matrix.
    rows = int(input("\nEnter the number of rows: "))
    columns = int(input("\nEnter the number of columns: "))

    # Read in elements into the matrix.
    for row in range(rows):
        line = input(f"\nEnter element of row {row} separated by space: ").strip().split()
        # terminates the program if the number of elements in a row is not equal to the number of columns.
        if len(line) != columns:
            print(f"\nUse {columns} elements in a row!")
            exit(2)
        matrix.append([eval(x) for x in line])

    # Checks if the sum of columns is equal to 1 and if every element is positive, Then displays the result.
    if checkSumOfColumns(matrix) and checkSign(matrix):
        print("\nThe matrix is a Markov matrix.")
    else:
        print("\nThe matrix is not a Markov matrix.")


if __name__ == "__main__":
    main()
