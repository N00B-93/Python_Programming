"""
    This is a program that uses a function with the header;
                def numberOfDaysInAYear(year):
    to determine the determine the number of days in years from 2010 to 2020.
"""


def numberOfDaysInAYear(year):
    """
    Returns the number of days in a year.

    :param year: (int) The year whose number of days is to be determined.

    :return: (int) Number of days in year.
    """
    
    # Returns 366 if year is leap else, returns 365.
    if year % 4 == 0 or year % 400 == 0:
        return 366
    else:
        return 365


def main():
    print("\nYear\t\tNumber Of Days")

    for year in range(2010, 2021):
        print(f"{year}\t\t{numberOfDaysInAYear(year):14}")


if __name__ == "__main__":
    main()

