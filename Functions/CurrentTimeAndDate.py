from time import time  # Importing the 'time' function from the 'time' module


def NumberOfLeapYearsAfterEpoch(numberOfYearsAfterEpoch):
    """
    Counts the number of leap years after the epoch till a given number of years.

    Args:
    numberOfYearsAfterEpoch (int): The number of years after the epoch.

    Returns:
    int: The count of leap years within the provided range of years.
    """
    counter = 0  # Initialize the counter for leap years
    # Loop through the range of years after the epoch
    for year in range(1970, (1970 + numberOfYearsAfterEpoch + 1)):
        # Check for leap year conditions and increment the counter if met
        if (year % 4 == 0 and year % 100 != 0) or (year % 100 == 0 and year % 400 == 0):
            counter += 1
    return counter  # Return the count of leap years


def getMonth(month):
    """
    Returns the name of the month based on its number.

    Args:
    month (int): The number representing the month (1 to 12).

    Returns:
    str: The name of the month.
    """
    # Using a 'match' statement to determine the month name based on its number
    match month:
        case 1: return "January"
        case 2: return "February"
        case 3: return "March"
        case 4: return "April"
        case 5: return "May"
        case 6: return "June"
        case 7: return "July"
        case 8: return "August"
        case 9: return "September"
        case 10: return "October"
        case 11: return "November"
        case 12: return "December"


def printCurrentTimeAndDate():
    """
    Prints the current date and time in a specific format.
    """
    totalSecond = int(time())  # Get the total number of seconds since the epoch
    currentSecond = totalSecond % 60  # Calculate the current second
    totalMinute = totalSecond // 60  # Calculate the total minutes
    currentMinute = totalMinute % 60  # Calculate the current minute
    totalHour = totalMinute // 60  # Calculate the total hours
    currentHour = totalHour % 24  # Calculate the current hour
    totalDays = totalHour // 24  # Calculate the total days

    numberOfYears = totalDays // 365  # Calculate the number of years ignoring leap years
    totalDays = totalDays + NumberOfLeapYearsAfterEpoch(numberOfYears)  # Adjust total days considering leap years

    currentDay = totalDays % 24  # Calculate the current day

    numberOfYears = totalDays // 366  # Recalculate the number of years considering leap years
    currentYear = numberOfYears + 1970  # Calculate the current year

    totalMonth = numberOfYears * 12
    currentMonth = totalMonth % 24  # This line seems to be missing a variable assignment

    # Print the calculated date and time in a specific format
    print(
        "\nCurrent Date and Time: ",
        getMonth(currentMonth),  # Get the month name based on the calculated currentMonth
        " ",
        currentDay,
        ", ",
        currentYear,
        " ",
        currentHour,
        ":",
        currentMinute,
        ":",
        currentSecond,
        sep=""
    )


if __name__ == "__main__":
    # Call the function to print the current time and date
    printCurrentTimeAndDate()

