"""
    This is a program that reads the subtotal and
    the gratuity rate and computes the gratuity and total.
"""

# Reads in the subtotal.
subtotal = float(input("\nEnter the subtotal: "))

# Reads in the gratuity rate.
gratuityRate = float(input("\nEnter the gratuity rate: "))

# Calculates the total.
total = subtotal + subtotal * (gratuityRate / 100)

# Calculates the gratuity
gratuity = subtotal * (gratuityRate / 100)

# Displays the results.
print(f"\nGratuity = {gratuity:.2f}")
print(f"\nTotal = {total:.2f}")
