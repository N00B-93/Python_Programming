"""
    This is a program that display a conversion table from kilograms to pounds
    and pounds to kilograms side by side.
"""

# defines starting point for each weight.
kilogram = 1
pounds = 20

# Prints the table heading.
print("\nKilogram\t\tPounds\t\tPounds\t\tKilograms")
for i in range(100):
    # Converts the weight from kilogram to pounds and pounds to kilogram and then displays the result.
    print(f"{kilogram}\t\t{kilogram * 2.2:14.2f}\t\t{pounds:6}\t\t{pounds * 0.45454:8.2f}")
    kilogram += 2
    pounds += 5
