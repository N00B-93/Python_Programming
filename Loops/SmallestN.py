from math import pow

"""
    This is a program that uses a while loop to find the smallest
    integer n such that n2 is greater than 12,000
"""

# Initailizes variable n to 0.
n = 0

# Loop that keeps running till n^2 > 12000.
while pow(n, 2) < 12000:
    n += 1

# Displays the result.
print(f"\nThe smallest n such that n^2 > 12000 is: {n - 1}")

