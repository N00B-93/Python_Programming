"""
    This is a program that prompts the user to enter the principal
    and the annual interest rate and then displays the displays the monthly interest.
"""

# Prompts the user to enter the principal.
principal = float(input("\nEnter the principal: $"))

# Prompts the user to enter the annual interest rate.
interestRate = float(input("\nEnter the annual interest rate(e.g. 3%): "))

# Computes the monthly interest.
monthlyInterest = principal * interestRate / 1200;

# Displays the result.
print(f"\nThe interest for the next month is: ${monthlyInterest:.2f}")
