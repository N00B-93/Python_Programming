from random import randint

"""
    This a program that generates two integers under 100 and
    prompts the user to enter the product of these two integers. The program then reports
    true if the answer is correct, false otherwise.
"""

# Generates two random numbers between 1 - 100.
number1 = randint(1, 100)
number2 = randint(1, 100)

# Calculates the sum of the numbers
sumOfNumbers = number1 * number2

# Prompts the user to enter the sum of the numbers.
answer = int(input(f"\nWhat is {number1} * {number2}? "))

# Informs the user if the solution he/she enters is right or wrong.
if answer == sumOfNumbers:
    print("\nCorrect!")
else:
    print("\nWrong!")
