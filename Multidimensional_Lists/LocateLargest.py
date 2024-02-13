"""
    This is a program that uses the function;
                def locateLargest(matrix)
    to determine the position of the largest element in a 2-Dimensional matrix.
"""


def locateLargest(matrix):
    """
    Returns the location of the largest element in a 2-Dimensional matrix.

    :param matrix: (list) A 2-Dimensional to be processed.

    :return: (list) The location of the largest element.
    """
    largestElement = 0
    largestElementIndex = []

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] > largestElement:
                largestElement = matrix[i][j]
                largestElementIndex = [i, j]
    return largestElementIndex


def main():
    # Creates an empty list to represent an array.
    matrix = []

    # Prompts the user to enter the number of rows and columns of the matrix.
    rows = int(input("\nEnter the number of rows: "))
    columns = int(input("\nEnter the number of columns: "))

    # Fills the matrix with elements.
    for row in range(rows):
        line = input(f"\nEnter the elements of row {row + 1}: ").strip().split()
        # terminates the program if the number of elements in a row is not equal to the number of columns.
        if len(line) != columns:
            print(f"\nUse {columns} elements in a row!")
            exit(2)
        matrix.append([eval(x) for x in line])

    # Determines the location of the largest element.
    largestElementIndex = locateLargest(matrix)

    print(f"\nThe largest element is located at position: {(largestElementIndex[0], largestElementIndex[1])}")


if __name__ == "__main__":
    main()
