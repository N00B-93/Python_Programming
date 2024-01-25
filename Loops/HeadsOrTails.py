from random import randint

"""
    This is a program that simulates flipping a coin one
    million times and displays the number of heads and tails.
"""
# Initializes heads and tails counter to 0.
heads, tails = 0, 0

for i in range(0, 1000000):
    # Generates a number from 0 to 1
    side = randint(0, 1)
    # Increments the heads and tails variables if side is 0 or side is 1.
    if side == 1:
        tails += 1
    elif side == 0:
        heads += 1

# Displays the result.
print(f"\nHeads: {heads}\nTails: {tails}")
