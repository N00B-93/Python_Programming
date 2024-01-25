"""
    This is a program that reads integers, finds the
    largest of them, and counts its occurrences. Assume that the input ends with number 0.
"""

# Reads in a number
number = int(input("\nEnter a number('0' to quit): "))

# Initializes maxNumber with the first number and set the counter to 1.
maxNumber = number
countOfMax = 1


while number != 0:
    number = int(input("\nEnter a number('0' to quit): "))

    # Updates the maxNumber and resets the counter to 1 if the current number is greater than the max number.
    if number > maxNumber:
        maxNumber = number
        countOfMax = 1
    elif number == maxNumber:  # Increments the counter by 1 if the current number is equal to the max number.
        countOfMax += 1

# Displays the result.
print(f"\nMax Number = {maxNumber}\nCount of Max Numbers = {countOfMax}")
