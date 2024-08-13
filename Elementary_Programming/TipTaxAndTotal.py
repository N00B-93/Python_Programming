"""
    This  is a program that prompts the user to enter the charge for food eaten in a restaurant and then calculates
    an 18% tip and a 7% sales tax.
    The program then displays the charge of the food, the tip, the sales tax and the total expenditure.
"""
# Prompts the user to enter the food charge.
foodCharge = float(input("\nEnter the food charge: $ "))

# Constants to hold the percentage tip and sales tax.
PERCENTAGE_TIP = 0.18
SALES_TAX = 0.07

# calculates the tip.
tip = PERCENTAGE_TIP * foodCharge

# Calculates the sales charge.
salesCharge = SALES_TAX * foodCharge

# Calculates the total expenditure.
totalExpenditure = foodCharge + tip + salesCharge

# Displays the Receipt.
print("\n****************Receipt****************")
print(f"\n\tFood Charge: $ {foodCharge:.2f}")
print(f"\n\tTip: $ {tip:.2f}")
print(f"\n\tSales Charge: $ {salesCharge:.2f}")
print(f"\n\tTotal Expenditure: $ {totalExpenditure:.2f}")
print("\n***************************************")
