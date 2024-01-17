from math import sqrt

"""
    This is a program that displays the square root of numbers from 0 to 20 in steps of 2.
"""

# Displays the result.
print(f"Number\t\tSquare Root")
for number in range(0, 21, 2):
    print(f"{number}\t\t{sqrt(number):11.4f}")
