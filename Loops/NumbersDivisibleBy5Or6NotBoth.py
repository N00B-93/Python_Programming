"""
    This is a program that displays, ten
    numbers per line, all the numbers from 100 to 200 that are divisible by 5 or 6, but
    not both. The numbers are separated by exactly one space.
"""

# Initializes the counter variable to 0.
counter = 0

for number in range(100, 201):
    # Prints a number if it's divisible by 5 or 6 but not both, else it moves to the next iteration.
    if (number % 5 == 0 or number % 6 == 0) ^ (number % 5 == 0 and number % 6 == 0):
        print(f"{number} ", end="")
        counter += 1  # Increments counter by 1.
    else:
        continue

    # Prints a new line if counter is a multiple of 10.
    if counter % 10 == 0:
        print()

