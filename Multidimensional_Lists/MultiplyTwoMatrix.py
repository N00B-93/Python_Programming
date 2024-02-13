"""
    This is a program that uses a function with the header;
                def multiplyMatrix(matrixA, matrixB)
    to calculate the product of two 3x3 matrices.
"""


def multiplyMatrix(matrixA, matrixB):
    """
    Returns a two-dimensional list holding the product of two 3x3 matrices.

    :param matrixA: (list) The first matrix.

    :param matrixB: (list) The second matrix.

    :return: (list) The product of two 3x3 matrices.
    """
    product = []
    k, j = 0, 0

    for row in range(3):
        matrixProduct = []
        col = 0
        while col < 3:
            matrixProduct.append(matrixA[row][k] * matrixB[j][col] + matrixA[row][k + 1] * matrixB[j + 1][col]
                                 + matrixA[row][k + 2] * matrixB[j + 2][col])
            col += 1
        row += 1
        product.append(matrixProduct)
    return product


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

    # Determines the product of the two matrix.
    matrix3 = multiplyMatrix(matrix1, matrix2)

    # Displays the result.
    print("\nThe product of the matrices is: ")
    print(f"{matrix1[0][0]} {matrix1[0][1]} {matrix1[0][2]}\t\t{matrix2[0][0]} {matrix2[0][1]} {matrix2[0][2]}\t"
          f"\t\t{matrix3[0][0]:.2f} {matrix3[0][1]:.2f} {matrix3[0][2]:.2f}\n"
          f"{matrix1[1][0]} {matrix1[1][1]} {matrix1[1][2]}\t*\t{matrix2[1][0]} {matrix2[1][1]} {matrix2[1][2]}\t"
          f"=\t{matrix3[1][0]:.2f} {matrix3[1][1]:.2f} {matrix3[1][2]:.2f}\n"
          f"{matrix1[2][0]} {matrix1[2][1]} {matrix1[2][2]}\t\t{matrix2[2][0]} {matrix2[2][1]} {matrix2[2][2]}\t"
          f"\t{matrix3[2][0]:.2f} {matrix3[2][1]:.2f} {matrix3[2][2]:.2f}")


if __name__ == "__main__":
    main()
