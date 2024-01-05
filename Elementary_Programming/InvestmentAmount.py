from math import pow

"""
    This a program that prompts the user to enter final account value, annual interest
    rate in percent, and the number of years, and displays the initial deposit amount.
"""

# Reads in thr final account value.
finalAccountValue = float(input("\nEnter the final account value: "))

# Reads in the annual interest rate in %
annualInterestRate = float(input("\nEnter the annual interest rate: ")) / 100.0

# Reads in the number of years.
years = int(input("\nEnter the number of years: "))

# Calculates the monthly interest rate.
monthlyInterestRate = annualInterestRate / 12

# Calculates the initial deposit.
initialDeposit = finalAccountValue / (pow(1 + monthlyInterestRate, years * 12))

# Displays the result.
print(f"\nThe initial deposit value is {initialDeposit:.2f}")
