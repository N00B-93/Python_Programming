"""This is a program that displays, ten numbers per line, all the numbers from 100 to 1,000 that are divisible by 5
and 6. The numbers are separated by exactly one space.
"""

# Initializes a counter variable.
counter = 0

for number in range(100, 1001):
    # Checks if the number is divisible by 5 and 6. If so, the number is printed followed by a space and the counter
    # variable is incremented.
    if number % 5 == 0 and number % 6 == 0:
        print(f"{number} ", end="")
        counter += 1
    else:
        continue

    # Prints a new line if the counter variable is a multiple of 10.
    if counter % 10 == 0:
        print()
