"""
    This is a program that displays all possible combinations for
    picking two numbers from integers 1 to 7. Also display the total number of combinations.
"""

# Variable used to count number of combinations.
counter = 0

for i in range(1, 7):
    for j in range(i + 1, 8):
        # Displays a combination and increments counter by 1.
        print(f"{i}, {j}")
        counter += 1
print(f"\nTotal number of combinations: {counter}")
