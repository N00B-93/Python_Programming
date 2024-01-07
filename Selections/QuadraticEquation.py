from math import sqrt, pow
from sys import exit

"""
    This is a program that prompts the user to enter values for a, b, and c for a quadratic equation and displays
    the result based on the discriminant. If the discriminant is positive, two roots are displayed. 
    If the discriminant is 0, one root is displayed. Otherwise, The equation has no real roots is displayed.
"""
# Reads in the values of the coefficients a, b, c.
a, b, c = eval(input("\nEnter the values of a, b, and c: "))

# Calculates the discriminant.
discriminant = pow(b, 2) - 4 * a * c

# Informs the user that the equation has no roots and exits the program if the discriminant < 0.
if discriminant < 0:
    print(f"\nThe equation has no real roots!")
    exit(0)

# Calculates the first root
root1 = (-b + sqrt(discriminant)) / (2 * a)

# Calculates the second root.
root2 = (-b - sqrt(discriminant)) / (2 * a)

# Displays the result depending on whether the discriminant is greater than 0 or equal to 0.
if discriminant > 0:
    print(f"\nThe roots are: {root1:.2f}, {root2:.2f}")
elif discriminant == 0:
    print(f"\nThe root is: {root1:.2f}")
