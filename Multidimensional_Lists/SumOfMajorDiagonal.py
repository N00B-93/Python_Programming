from sys import exit


"""
    This is a program that uses a function with the header;
                def sumMajorDiagonal(matrix)
    to calculate the sum of elements in the major diagonal of a square matrix.
"""


def sumMajorDiagonal(matrix):
    """
    Returns the sum of elements in the major diagonal of a matrix.

    :param matrix: (list) The matrix whose sum of major diagonal is to be determined.

    :return: (float) The sum of the major diagonal of the matrix.
    """
    total = 0

    for row in range(len(matrix)):
        for column in range(len(matrix[0])):
            if row == column:
                total += matrix[row][column]
    return total


def main():
    # Creates a empty list to represent a matrix.
    matrix = []

    # Read in the number or rows and columns.
    rows = int(input("\nEnter the number of rows: "))
    columns = int(input("\nEnter the number of columns: "))
    
    # Terminates the program of the number of rows is not equal to the number of columns.
    if rows != columns:
        print("\nThe number of row must equal number of columns.")
        exit(1)
    
    # Fills the matrix with elements.
    for row in range(rows):
        line = input(f"\nEnter the elements of row {row + 1}: ").strip().split()
        matrix.append([eval(x) for x in line])

    # Displays the result.
    print(f"\nThe sum of elements in the major diagonal is: {sumMajorDiagonal(matrix)}")

    
if __name__ == "__main__":
    main()

