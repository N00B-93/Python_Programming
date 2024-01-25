"""
    A positive integer is called a perfect number if it is equal to the
    sum of all of its positive divisors, excluding itself.
    This is a program that displays all the perfect numbers from 1 to 10000.
"""

number = 2

while number <= 10000:
    # Re-initializes the factors and sumOfFactors variable to 1 and 0 respectively.
    factor = 1
    sumOfFactors = 0

    while factor <= number / 2:
        # Sums the factors of a number.
        if number % factor == 0:
            sumOfFactors += factor
        factor += 1
    # Displays the number if the sum of its factors is the same as the number.
    if sumOfFactors == number:
        print(f"\n{number} is a perfect number.")
    # Increments the number by 1.
    number += 1

