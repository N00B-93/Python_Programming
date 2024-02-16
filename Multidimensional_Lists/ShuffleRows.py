from random import randint

"""
    This is a program that uses a function with the header;
                def shuffle(matrix)
    to shuffle the rows in the two dimensional list given below;
                m = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
"""


def shuffle(matrix):
    """
    Shuffles the rows in a given two-dimensional list.

    :param matrix: (list) The two-dimensional list to the processed.

    :return: None.
    """
    previousRow = 0

    for i in range(len(matrix)):
        currentRow = randint(0, len(matrix) - 1)
        while previousRow == currentRow:
            currentRow = randint(0, len(matrix) - 1)
        matrix[i], matrix[currentRow] = matrix[currentRow], matrix[i]

        previousRow = currentRow


def main():
    # The matrix to be shuffled.
    matrix = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]

    # Displays the matrix.
    print("\nThe original matrix is: ")
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            print(f"{matrix[row][column]} ", end="")
        print()

    # Shuffles the given matrix.
    shuffle(matrix)
    
    # Displays the shuffled matrix.
    print("\nThe shuffled matrix is: ")
    [[print(f"{matrix[row][column]} ", end="") for column in range(len(matrix[row]))]
     and print() or row for row in range(len(matrix))]


if __name__ == "__main__":
    main()
