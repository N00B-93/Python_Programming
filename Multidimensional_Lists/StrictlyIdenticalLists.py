"""
    Two lists are strictly identical if their corresponding elements are equal.
    This is a program that uses the function with the header;
                def equals(matrix1, matrix2)
    to check if two 3x3 matrices are strictly identical.
"""


def equals(matrix1, matrix2):
    """
    Check if two 3x3 matrices are strictly identical.

    :param matrix1: (list) The first 3x3 matrix to be compared.

    :param matrix2: (list) The second 3x3 matrix to be compared.

    :return: (bool) True if two 3x3 matrices are strictly identical else False.
    """
    for row in range(3):
        for col in range(3):
            if matrix1[row][col] != matrix2[row][col]:
                return False
    return True


def main():
    matrix1, matrix2 = [], []

    # Reads in the element of the first matrix.
    print("\nEnter the elements of the first matrix.")
    for row in range(3):
        line = input(f"\nEnter element of row {row} separated by space: ").strip().split()
        # terminates the program if the number of elements in a row is not equal to the number of columns.
        if len(line) != 3:
            print("\nUse 3 elements in a row!")
            exit(2)
        matrix1.append([eval(x) for x in line])

    # Reads in the element of the second matrix.
    print("\nEnter the elements of the second matrix.")
    for row in range(3):
        line = input(f"\nEnter element of row {row} separated by space: ").strip().split()
        # terminates the program if the number of elements in a row is not equal to the number of columns.
        if len(line) != 3:
            print("\nUse 3 elements in a row!")
            exit(2)
        matrix2.append([eval(x) for x in line])

    # Checks if the Matrices are strictly identical.
    isStrictlyIdentical = equals(matrix1, matrix2)

    # Displays the result.
    if isStrictlyIdentical:
        print("\nThe lists are Strictly identical!")
    else:
        print("\nThe lists are not Strictly identical!")


if __name__ == "__main__":
    main()
