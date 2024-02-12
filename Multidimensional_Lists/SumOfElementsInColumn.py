"""
    This is a program that uses a method with a header;
                def sumColumn(matrix, columnIndex)
    to find the sum of elements in a specified column of a matrix.
"""


def sumColumn(matrix, columnIndex):
    """
    Returns the sum of elements in a column of a matrix.

    :param matrix: (list) The matrix containing elements.

    :param columnIndex: (int) The index of the column whose elements are to be summed.

    :return: (float) The sum of elements in a column.
    """
    total = 0

    for row in range(len(matrix)):
        total += matrix[row][columnIndex]
    return total


def main():
    # Creates an empty list representing a matrix.
    matrix = []

    # Reads in the number of rows and colunns of the matrix.
    rows = int(input("\nEnter the number of rows: "))
    columns = int(input("\nEnter the number of columns: "))
    
    # Read in elements into the matrix.
    for row in range(rows):
        line = input(f"\nEnter element of row {row} separated by space: ").strip().split()
        matrix.append([eval(x) for x in line])

    # Reads in the index of the column whose sum of element is to he determined.
    columnIndex = int(input("\nEnter the index of the column whose sum is to be calculated: "))

    # Displays the result.
    print(f"\nThe sum of element in column {columnIndex} is: {sumColumn(matrix, columnIndex):.2f}")


if __name__ == "__main__":
    main()

