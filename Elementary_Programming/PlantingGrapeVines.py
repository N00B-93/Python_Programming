"""
    A vineyard owner is planting several new rows of grapevines, and needs to know how many
    grapevines to plant in each row. She has determined that after measuring the length of a
    future row, she can use the following formula to calculate the number of vines that will fit
    in the row, along with the trellis end-post assemblies that will need to be constructed at
    each end of the row:
                    V = (R - 2E) / S

    The terms in the formula are:
        V is the number of grapevines that will fit in the row.
        R is the length of the row, in feet.
        E is the amount of space, in feet, used by an end-post assembly.
        S is the space between vines, in feet.

    This program prompts the user to enter;
        • The length of the row, in feet
        • The amount of space used by an end-post assembly, in feet
        • The amount of space between the vines, in feet
    then calculate and display the number of grapevines that will fit in the row.
"""

# Prompts the user to enter the length of the rows in feet.
lengthOfRow = float(input("\nEnter the length of the row, in feet: "))

# Prompts the user to enter the amount of space used by the end post in feet.
amountOfSpaceUsedByEndPost = float(input("\nEnter the amount of space used by an end-post, in feet: "))

# Prompts the user to enter the amount of space between vines in feet.
amountOfSpaceBetweenVines = float(input("\nEnter the amount of space between the vines, in feet: "))

# Calculates the number of grapevines in a row.
numberOfGrapevinesInARow = (lengthOfRow - 2 * amountOfSpaceUsedByEndPost) / amountOfSpaceBetweenVines

# Displays the result.
print(f"\nThe amount of grapevines in the row is {int(numberOfGrapevinesInARow)} grapevines.")
