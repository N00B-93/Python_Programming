"""
    This is a program that prompts the user to enter
    the minutes (e.g., 1 billion), and displays the number of years and days for
    the minutes.
"""
# Reads in the minute.
minutes = int(input("\nEnter the number of minutes: "))

# Constant to hold the number of minutes in a year.
MINUTES_IN_A_YEAR = 525600

# Calculates the years.
years = minutes // MINUTES_IN_A_YEAR

# Constant to hold the number of minutes in a day.
MINUTES_IN_A_DAY = 1440

# Calculates the days.
days = (minutes % 525600) // MINUTES_IN_A_DAY

# Displays the result.
print(f"\n{minutes} minutes is approximately {years} years and {days} days")
