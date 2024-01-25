"""
    This is a program that lets the user enter the loan amount and loan period and number of years
    and displays the monthly and total payments for each interest rate starting from
    5% to 8%, with an increment of 1/8.
"""
# Reads in the loan amount and number of years.
loanAmount = float(input("\nEnter the loan amount: "))
years = int(input("\nEnter the number of years: "))

interestRate = 0.05

print("\nInterest Rate\t\tMonthly Payment\t\tTotal Payment")

while interestRate <= 0.081:
    # Calculates the monthly interest rate.
    monthlyInterestRate = interestRate / 12

    # Calculates the monthly payment.
    monthlyPayment = loanAmount * monthlyInterestRate / (1 - 1/(1 + monthlyInterestRate) ** (12 * years))

    # Calculates the total payment.
    totalPayment = monthlyPayment * years * 12

    # Displays the result.
    print(f"{interestRate:13.3f}\t\t{monthlyPayment:15.3f}\t\t{totalPayment:13.3f}")

    # Increments interest rate by 0.00125.
    interestRate += 0.00125
