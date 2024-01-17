"""
    This is a program that converts distance from Miles to Kilometers
    and displays the result in tabular form.
"""

miles = 1.609  # Conversion rate from miles to kilometer.

# Displays the result.
print("\nMiles\t\tKilometers")
for i in range(1, 11):
    print(f"{i}\t\t{i * 1.609:10.2f}")

