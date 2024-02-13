from random import randint

"""
    This is a program that randomly fills in 0s and 1s into
    a matrix, prints the matrix, and finds the rows and columns with the most 1s.
"""


def countOnesInColumns(matrix):
    """
    Returns the index of the column that has the highest number of 1's

    :param matrix: (list) The matrix to be processed.

    :return: (list) The list containing the indices with the highest number of 1's
    """
    counter = 0
    counterList = []

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[j][i] == 1:
                counter += 1
        counterList.append(counter)
        counter = 0

    maxIndex = []
    return [maxIndex.append(i) or i for i in range(len(counterList)) if counterList[i] >= max(counterList)]


def countOnesInRows(matrix):
    """
    Returns the index of the row that has the highest number of 1's

    :param matrix: (list) The matrix to be processed.

    :return: (list) The list containing the indices with the highest number of 1's
    """
    counter = 0
    counterList = []

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                counter += 1
        counterList.append(counter)
        counter = 0

    maxIndex = []
    return [maxIndex.append(i) or i for i in range(len(counterList)) if counterList[i] >= max(counterList)]


def main():
    # Creates a nested list to store a 4x4 matrix.
    matrix = [[], [], [], []]

    # Appends 1's or 0's randomly in the matrix.
    for i in range(len(matrix)):
        for j in range(4):
            matrix[i].append(randint(0, 1))

    # Determines the row(s) and column(s) with the most number of 1's
    lst1 = countOnesInColumns(matrix)
    lst2 = countOnesInRows(matrix)

    # Displays the generated 4x4 matrix.
    print("\nThe generated matrix is: ")
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            print(f"{matrix[i][j]} ", end="")
        print()

    # Displays the column(s) with the largest number of 1's
    print("\nThe column(s) with largest number of 1's: ", end="")
    [print(f"{lst1[i]} ", end="") or i for i in range(len(lst1))]
    print()

    # Displays the row(s) with the largest number of 1's
    print("\nThe row(s) with largest number of 1's: ", end="")
    [print(f"{lst2[i]} ", end="") or i for i in range(len(lst2))]
    print()


if __name__ == "__main__":
    main()
