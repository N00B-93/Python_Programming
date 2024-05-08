"""
    The Fibonacci sequence starts 1, 1, 2, 3, 5, 8, .. . . Each number in the sequence (after the first
    two) is the sum of the previous two. This is a program that computes and outputs the nth Fibonacci 
    number, where n is a value entered by the user.
"""

# Prompts the user to enter a number.
number = input("\nEnter a number for n = 0, 1, 2, ...: ")

# Displays an error message and continue to prompt the user to enter a correct input if user input is invalid.
while not number.isdigit() or int(number) < 0:
    print(f"\nError: Use a number greater than 0, Try again.")
    number = input("\nEnter a number representing the nth term of the Fibonacci sequence: ")

previousTerm, currentTerm, nextTerm = 0, 1, 0

# Displays the Fibonacci number at the 0th or 1st index respectively depending on the user's input.
if int(number) == 0 or int(number) == 1:
    print(f"\nThe Fibonacci number at index {number} is: {number}\n")
    exit(0)

# Determines the Fibonacci number at the nth index.
for i in range(int(number) - 1):
    nextTerm = previousTerm + currentTerm
    previousTerm = currentTerm
    currentTerm = nextTerm

# Displays the Fibonacci number at the index entered by the user.
print(f"\nThe Fibonacci number at index {number} is: {nextTerm}\n")
