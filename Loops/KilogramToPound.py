"""
    This is a program that displays a conversion table that shows the conversion of weight from
    kilograms to pounds.
"""

# Defines the conversion rate from kilograms to pounds.
kilogramToPounds = 2.2

# Displays the result in a tabular form.
print("\nKilograms\t\tPounds")
for i in range(1, 200, 2):  # For loop that runs from 1 to 200 with a step of 2.
    print(f"{i}\t\t{i * kilogramToPounds:14.2f}\t\t")
