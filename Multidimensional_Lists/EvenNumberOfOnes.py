from random import randint

"""
    This is a program that generates a two-dimensional matrix filled with 0s and 1s, 
    displays the matrix, and checks to see if every row
    and every column has an even number of 1s.

"""


def checkRows(matrix):
    """
    Checks if all rows in a 6x6 matrix contains an even number of 1's.

    :param matrix: (list) The matrix whose rows are to be checked.

    :return: (list) A list containing boolean value that represents whether each row has even number of 1's or not.
    """
    return [matrix[row].count(1) % 2 == 0 for row in range(len(matrix))]


def checkColumns(matrix):
    """
    Checks if all columns in a 6x6 matrix contains an even number of 1's.

    :param matrix: (list) The matrix whose columns are to be checked.

    :return: (list) A list containing boolean value that represents whether each row has even number of 1's or not.
    """
    lst = []
    
    for col in range(len(matrix)):
        counter = 0
        for row in range(len(matrix)):
            if matrix[row][col] == 1:
                counter += 1
        lst.append(True) if counter % 2 == 0 else lst.append(False)
    return lst


def main():
    # Creates an empty list.
    matrix = []
    
    # Fills the matrix list with randomly generated numbers(0's and 1's).
    for i in range(6):
        lst = []
        for j in range(6):
            lst.append(randint(0, 1))
        matrix.append(lst)

    # Displays the matrix.
    [[print(f"{matrix[i][j]} ", end="") or j for j in range(len(matrix[i]))] and print() or i for i in range(len(matrix))]

    # Checks if all rows contains an even number of 1's.
    lst1 = checkRows(matrix)
    lst2 = checkColumns(matrix)

    print(lst1)
    print(lst2)
    
    # Displays the result.
    if all(lst1) and all(lst2):
        print("\nAll rows and columns has an even number of 1's")
    elif all(lst1) and not all(lst2):
        print("\nOnly all the rows have even number of 1's")
    elif all(lst2) and not all(lst1):
        print("\nOnly all columns have even number of 1's")
    else:
        print("\nNo row or column have even number of 1's")


if __name__ == "__main__":
    main()

