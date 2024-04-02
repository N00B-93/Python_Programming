"""
    This is a program that prompts the user to enter the electric charge on two charged particles and the
    distance between them and then calculates the electric force between them using Coulomb's law.
"""


# The permutivity of free space constant.
PERMUTIVITY_OF_FREE_SPACE = 8.854e-12

# Reads in the magnitude of the first charge.
q1 = float(input("\nEnter the value of the first charge: "))

# Reads in the magnitude of the second charge.
q2 = float(input("\nEnter the value of the second charge: "))

# Reads in the distance between the charges.
r = float(input("\nEnter the distance between the charges: "))

# Calculates the force of attraction(or repulsion) between charges.
forceBetweenCharges = (PERMUTIVITY_OF_FREE_SPACE * q1 * q2) / r

# Displays the result.
if forceBetweenCharges > 0:
    print("\nThe force of attraction between the charges is", format(forceBetweenCharges, ".3e"), 'N')
else:
    print("\nThe force of repulsion between the charges is", format(forceBetweenCharges, ".3e"), 'N')

