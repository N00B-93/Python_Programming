"""
    This is a program that displays all the leap years from 2001 to 2100 separated by exactly one
    space and printed ten per line.
"""
# Initializes the lineCounter variable.
lineCounter = 0

for year in range(2001, 2101):
    # Displays a year if the year is an ordinary year and  is outrightly divisible by 4 or if the year is a millennial
    # year and is outrightly divisible by 400.
    if (year % 4 == 0 and year % 400 != 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} ", end="")
        # Increments the linCounter variable by 1.
        lineCounter += 1
        if lineCounter % 10 == 0:
            # Displays a newline if the lineCounter variable is a multiple of 10.
            print()
