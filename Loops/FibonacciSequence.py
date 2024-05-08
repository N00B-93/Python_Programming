"""
    The Fibonacci sequence starts 1, 1, 2, 3, 5, 8, .. . . Each number in the sequence (after the first
    two) is the sum of the previous two. This is a program that computes and outputs the nth Fibonacci 
    number, where n is a value entered by the user.
"""

# Prompts the user to enter a number.
number = input("\nEnter a number representing the nth term of the Fibonacci sequence: ")

# Displays an error message and continue to prompt the user to enter a correct input if user input is invalid.
while int(number) < 0:
    print(f"\nError: Use a number greater than 0, Try again.")
    number = input("\nEnter a number representing the nth term of the Fibonacci sequence: ")


