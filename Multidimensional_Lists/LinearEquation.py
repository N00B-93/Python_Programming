"""
    This is a program that uses a function with the header;
                def linearEquation(a, b)
    to solve the 2x2 system of linear equation given below;
                a00x + a01y = b0
                a10x + a11y = b1
"""


def linearEquation(a, b):
    """
    Solves a system of linear equations of the form Ax +By = C.

    Parameters:
    - a (list of lists): Coefficients matrix A, where each inner list represents a row.
    - b (list): Constants vector B.

    Returns:
    - tuple or None: If the system has a unique solution, returns a tuple (x, y) representing the solution.
      If the system is inconsistent or has infinitely many solutions, returns None.
    """
    # Calculate the determinant of matrix A
    denominator = a[0][0] * a[1][1] - a[1][0] * a[0][1]

    # Check if the system is consistent (denominator is not zero)
    if denominator == 0:
        return None
    
    # Calculate the solution (x, y)
    x = (b[0] * a[1][1] - b[1] * a[0][1]) / denominator
    y = (a[0][0] * b[1] - a[1][0] * b[0]) / denominator

    return x, y


def main():
    # Reads in the coefficients of the linear equation.
    a00, a01, b0 = eval(input("\nEnter the values of a00, a01, b0 separated by comma: "))
    a10, a11, b1 = eval(input("\nEnter the values of a10, a11, b1 separated by comma: "))
    
    # Constructs two lists to hold the coefficients of the equation.
    a, b = [[a00, a01], [a10, a11]], [b0, b1]
    
    # Determines the roots of the equation and prints them.
    if linearEquation(a, b) is None:
        print("\nThe equation has no roots.")
    else:
        x, y = linearEquation(a, b)
        print(f"\nThe roots of the equation are: {x:.2f}, {y:.2f}")


if __name__ == "__main__":
    main()

