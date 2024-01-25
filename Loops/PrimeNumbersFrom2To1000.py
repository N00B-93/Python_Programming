"""
    This program display all the prime numbers between 2 and 1,000, inclusive
    eight per line.
"""

# Variable used to count lines.
lineCounter = 0

# Variable that holds the starting point
number = 2

while number <= 1000:
    # Sets the isPrime variable to True and the divisor variable to 2.
    isPrime = True
    divisor = 2

    while divisor <= (number / 2):
        # Sets the isPrime variable to False and exits the inner loop if the current number is not prime.
        if number % divisor == 0:
            isPrime = False
            break

        # Increments the divisor by 1.
        divisor += 1

    if isPrime:
        # Prints the number and increments the lineCounter variable by 1 if the number is prime.
        print(f"{number} ", end="")
        lineCounter += 1

        # Prints a newline if the lineCounter variable is a multiple of 8.
        if lineCounter % 8 == 0:
            print()

    # Increments the current number by 1.
    number += 1
