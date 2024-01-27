from math import pow

"""
    This is a program that computes the value of PI using the formula:
        PI = 4(1 - 1/3 + 1/5 - 1/7 + 1/9 - 1/11 + ... + (-1 ^(i + 1) / 2i - 1)
    and displays the value of PI for i = 10000, 20000,  ..., 100000.
"""

# Initializes PI to 0
PI = 0

print("\ti\t\tPI")
for i in range(10000, 100001):
    if i % 10000 == 0:
        for j in range(1, i):
            # Calculates the value of PI from 1 to i.
            PI += 4 * pow(-1, j + 1) / (2 * j - 1)
        # Displays the value of PI if i is a multiple of 10000.
        print(f"{i}\t\t{PI}")
    # Resets the value of PI to 0.
    PI = 0
