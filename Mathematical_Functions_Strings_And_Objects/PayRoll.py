"""
    This is a  program that reads the following information and prints a payroll statement:
        Employee’s name (e.g., Smith)
        Number of hours worked in a week (e.g., 10)
        Hourly pay rate (e.g., 9.75)
        Federal tax withholding rate (e.g., 20%)
        State tax withholding rate (e.g., 9%)
"""

# Reads in Employee Details.
employee_name = input("\nEnter employee name: ")
numberOfHours = int(input("\nEnter number of hours worked in a week: "))
hourlyPayRate = float(input("\nEnter hourly pay rate: "))
federalTaxWithholdingRate = float(input("\nEnter federal tax withholding rate (e.g. 3%): "))
stateTaxWithholdingRate = float(input("\nEnter state tax withholding rate (e.g. 3%): "))

# Calculates the federal withholding, state withholding and gross pay
federalWithholding = federalTaxWithholdingRate * hourlyPayRate * numberOfHours
stateWithholding = stateTaxWithholdingRate * hourlyPayRate * numberOfHours
grossPay = hourlyPayRate * numberOfHours

# Displays the Employee Details.
print(f"Employee Name: {employee_name}")
print(f"Hours worked: {numberOfHours}")
print(f"Pay rate: $ {hourlyPayRate}")
print(f"Gross pay: {grossPay:.2f}")
print("Deductions:")
print(f"\tFederal Withholding {federalTaxWithholdingRate:.2%}: $ {federalWithholding}")
print(f"\tState Withholding {stateTaxWithholdingRate:.2%}: $ {stateWithholding}")
print(f"\tTotal Deduction: $ {federalWithholding + stateWithholding}")
print(f"Net Pay: $ {grossPay - (federalWithholding + stateWithholding):.2f}")
