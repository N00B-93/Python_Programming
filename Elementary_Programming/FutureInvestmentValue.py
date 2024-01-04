from math import pow

"""
   This is a program that reads in an investment amount, th e annual interest rate,
   and the number of years, and displays the future investm ent value.
"""

# Reads in the investment amount.
investmentAmount = float(input("\nEnter the investment amount: "))

# Reads in the annual interest rate.
annualInterestRate = float(input("\nEnter the annual interest rate: ")) / 100.0

# Reads in the number of years.
years = int(input("\nEnter the number of years: "))

# Calculates the monthly interest rate.
monthlyInterestRate = annualInterestRate / 12

# Calculates the future investment value.
futureInvestmentValue = investmentAmount * pow(1 + monthlyInterestRate, years * 12)

# Displays the result.
print(f"\nAccumulated value is: {futureInvestmentValue:.2f}")

