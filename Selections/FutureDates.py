"""
    This is a program that prompts the user to enter an integer for
    today’s day of the week (Sunday is 0, Monday is 1, ..., and Saturday is 6). It also prompts
    the user to enter the number of days after today for a future day and displays
    the future day of the week.
"""

# Prompts the user to enter a number representing the current day.
today = int(input("\nEnter today's day: "))

# Prompts the user to enter the number of days elapsed after the current day.
numberOfDaysElapsed = int(input("\nEnter number of days elapsed since today: "))

# Calculates the future day.
futureDay = numberOfDaysElapsed % 7 + today

# Match-Case statements that displays the results.
match today:
    case 0:
        print("\nToday is Sunday", end=' ')
    case 1:
        print("\nToday is Monday", end=' ')
    case 2:
        print("\nToday is Tuesday", end=' ')
    case 3:
        print("\nToday is Wednesday", end=' ')
    case 4:
        print("\nToday is Thursday", end=' ')
    case 5:
        print("\nToday is Friday", end=' ')
    case 6:
        print("\nToday is Saturday", end=' ')

match futureDay:
    case 0:
        print("and future day is Sunday")
    case 1:
        print("and future day is Monday")
    case 2:
        print("and future day is Tuesday")
    case 3:
        print("and future day is Wednesday")
    case 4:
        print("and future day is Thursday")
    case 5:
        print("and future day is Friday")
    case 6:
        print("and future day is Saturday")
