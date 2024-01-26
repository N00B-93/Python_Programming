from math import pow
from sys import exit


"""
    This is a program that prompts the user to enter the investment amount and the
annual interest rate in percent and prints a table that displays the future value for
the years from 1 to 30 using a function with the header;

                def futureInvestmentValue(investmentAmount, monthlyInterestRate, years)
"""


def futureInvestmentValue(investmentAmount, monthlyInterestRate, year):
    """
    Calculates the future value of the amount invested for the year(s) specified.
    :param investmentAmount: (float) The amount invested.

    :param monthlyInterestRate: (float) The monthly interest rate on the amount invested.

    :param year: (int) The number of year in which the investment will be made.

    :return: (float) The future value for the year specified.
    """

    return investmentAmount * pow((1 + monthlyInterestRate), year * 12)


def main():
    # Reads in the amount to be invested.
    investmentAmount = float(input("\nEnter the amount invested: "))

    # Displays an error message and terminates the program if investmentAmount < 0.
    if investmentAmount < 0:
        print("\nPositive investment amount required.")
        exit(1)

    # Reads in the annual interest rate.
    annualInterestRate = float(input("\nEnter the annual interest rate in percent(e.g., 4%): ")) / 100

    # Terminates the program if the annualInterestRate < 0.
    if annualInterestRate < 0:
        print("\nPositive annual interest required.")
        exit(2)

    # Calculates monthly interest rate
    monthlyInterestRate = annualInterestRate / 12

    # Displays the year and future value of the investment in tabular form for 30 years.
    print("\nYear\t\tFuture Value")
    for i in range(1, 31):
        print(f"{i}\t\t{futureInvestmentValue(investmentAmount, monthlyInterestRate, i):16.2f}")


if __name__ == "__main__":
    main()
