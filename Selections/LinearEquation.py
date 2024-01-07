from sys import exit

"""
    Cramer’s rule can be used to solve the following 2 x 2 system of linear equation:
            ax + by = e     x = ed - bf / ad - bc
            cx + dy = f     y = af - ec / ad - bc
    This is a program that prompts the user to enter a, b, c, d, e, and f and display the
    result. If ad – bc is 0, it reports that The equation has no solution.
"""

# Reads in the values of the coefficients a, b, c, d, e, f.
a, b, c, d, e, f = eval(input("\nEnter the values of a, b, c, d, e and f respectively separated by comma: "))

# Calculates the value of the denominator.
denominator = a * d - b * c

# Informs the user that the equation has no real roots if the denominator is 0 and exits the program.
if denominator == 0:
    print("\nThe equation has no solution.")
    exit(0)

# Calculates the value of x.
x = (e * d - b * f) / denominator

# Calculates the value of y.
y = (a * f - e * c) / denominator

# Displays the result.
print(f"\nx = {x:.2f} and y = {y:.2f}")
