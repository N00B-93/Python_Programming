from random import randint
from time import time

"""
    This is a program that generates 10 addition questions and the prompts the user to enter the answer.
    The number of questions answered correctly and the time taken to complete the test are then displayed.
"""

# Initializes a variable to store the number of questions answered correctly.
correctCount = 0

# Determines the start time.
startTime = int(time())

for i in range(1, 11):
    # Generates two random numbers from 1 to 15
    number1 = randint(1, 15)
    number2 = randint(1, 15)

    # Prompts the user to enter the answer.
    answer = int(input(f"\nWhat is {number1} + {number2}? "))

    # Increments the correctCount variable by 1 if the answer entered is correct.
    if answer == number1 + number2:
        correctCount += 1

# Determines the stop time.
stopTime = int(time())

# Displays the result.
print(f"\nYou correctly answered: {correctCount} questions\nThe test took: {stopTime - startTime} secs.")
