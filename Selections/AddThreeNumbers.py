from random import randint

"""
    This program generates three single-digit integers and prompt the user to enter the sum of these three
    integers.
"""

# Generates three single-digit random numbers.
number1 = randint(1, 9)
number2 = randint(1, 9)
number3 = randint(1, 9)

# Calculates the sum of the numbers.
sumOfNumbers = number1 + number2 + number3

# Prompts the user to enter the solution of the sum of the three integers.
answer = int(input(f"\nWhat is {number1} + {number2} + {number3}? "))

# Informs the user if the solution he/she enters is right or wrong.
if answer == sumOfNumbers:
    print("\nThat's right!")
else:
    print("\nWrong!")
