"""
    This is a program that prompts the user to enter
    the minutes (e.g., 1 billion), and displays the number of years and days for
    the minutes.
"""
# Reads in the minute.
minutes = int(input("\nEnter the number of minutes: "))

# Calculates the years.
years = minutes // 525600

# Calculates the days.
days = (minutes % 525600) // 1440

# Displays the result.
print(f"\n{minutes} minutes is approximately {years} years and {days} days")
