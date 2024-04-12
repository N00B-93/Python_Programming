"""
    An employee’s total weekly pay equals the hourly wage multiplied by the total 
    number of regular hours plus any overtime pay. Overtime pay equals the total 
    overtime hours multiplied by 1.5 times the hourly wage.
    This is a program that takes as inputs the hourly wage, total regular hours, and total overtime 
    hours and displays an employee’s total weekly pay.
"""


# Reads in the user's hourly wage.
hourlyWage = float(input("\nEnter Hourly wage: $ "))

# Reads in the total regular hours.
regularHours = float(input("\nEnter total regular hours: "))

# Reads in total overtime hours.
overtimeHours = float(input("\nEnter total overtime hours: "))

# Determines the pay for regular hours.
regularPay = regularHours * hourlyWage

# Determines the overtime pay.
overtimePay = 1.5 * overtimeHours * hourlyWage

# Determines the user's total pay.
totalPay = regularPay + overtimePay

# Displays the result.
print(f"\nThe weekly pay is: ${totalPay: .2f}")

