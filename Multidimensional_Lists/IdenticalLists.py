"""
    Two 2-dimensional lists are identical if they have the same content.
    This is a program that uses a function with the header;
                def equals(list1, list2)
    to check whether the two 2-dimensional lists entered by the user are the same.
"""


def equals(list1, list2):
    """
    Checks if two 2-dimensional lists contains the same content.

    :param list1: (list) The first 2-dimensional list to compare.

    :param list2: (list) The second 2-dimensional list to compare.

    :return: (bool) True if the two 2-dimensional lists are identical, false otherwise.
    """
    [list1[row].sort() for row in range(len(list1))]
    [list2[row].sort() for row in range(len(list2))]

    return list1 == list2


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

    # Checks if the two lists are identical.
    isIdentical = equals(matrix1, matrix2)

    # Displays the result.
    if isIdentical:
        print("\nThe two lists are identical!")
    else:
        print("\nThe two lists are not identical!")


if __name__ == "__main__":
    main()
