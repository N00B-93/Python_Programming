def convertMillis(milliSeconds):
    """
    Converts milliseconds to hours:minutes:seconds format.

    Args:
    milliSeconds (int): The input milliseconds to be converted.

    Returns:
    str: A string representing the time in the format 'hour:minute:second'.
    """

    # Calculate the time components: hours, minutes, and seconds
    second = milliSeconds // 1000
    currentSecond = second % 60

    minute = second // 60
    currentMinute = minute % 60

    hour = minute // 60

    # Return the time in the format 'hour:minute:second' as a string
    return str(hour) + ":" + str(currentMinute) + ":" + str(currentSecond)


def main():
    """
    Main function to get user input and display converted time.
    """

    # Get user input for milliseconds
    millis = eval(input("\nEnter milliseconds to be converted: "))

    # Display the converted time in hours:minutes:seconds format
    print("\n", millis, " converted to hours:minutes:seconds is: ", convertMillis(millis), sep="")


if __name__ == "__main__":
    main()

