from sys import exit

"""
    This is a program that prompts the user to enter a year, month, and day of the
    month, and then it displays the name of the day of the week using Zeller's congruence.
"""

# Prompts the user to enter the year, month and day of the month.
year = int(input("\nEnter year(e.g., 2008): "))
month = int(input("\nEnter month(1 - 12): "))
day = int(input("\nEnter day of the month(1 - 31): "))

# Ensures the user enters a valid day or year.
if (month < 1 or month > 12) or (day < 1 or day > 31):
    print("\nInvalid day or month\nTry again.")
    exit(0)

# Changes user month input from 1 or 2 to 2 or 13 and the reduces the year by 1.
match month:
    case 1:
        month = 13
        year = year - 1
    case 2:
        month = 14
        year = year - 1

# Calculates the Century.
century = year // 100

# Calculate the year of the Century.
yearOfCentury = year % 100

# Calculates the day of the week.
dayOfWeek = day + 13 * (month + 1) // 5 + yearOfCentury + yearOfCentury // 4 + century // 4 + 5 * century
dayOfWeek %= 7

# Matches the number representing the day of the week to the appropriate day.
match dayOfWeek:
    case 0:
        dayOfWeek = 'Saturday'
    case 1:
        dayOfWeek = 'Sunday'
    case 2:
        dayOfWeek = 'Monday'
    case 3:
        dayOfWeek = 'Tuesday'
    case 4:
        dayOfWeek = 'Wednesday'
    case 5:
        dayOfWeek = 'Thursday'
    case 6:
        dayOfWeek = 'Friday'

# Displays the result.
print(f"\nThe day of the week is: {dayOfWeek}")
