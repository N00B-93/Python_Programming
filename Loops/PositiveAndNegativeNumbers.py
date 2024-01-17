"""
    This is a program that reads an unspecified number of integers, determines
    how many positive and negative values that have been read, and computes the total
    and average of the input values (not counting zeros). The input stops on entering 0.
"""

# Initializes the variables holding the number of positive entries, negative entries and sum of all entries.
numberOfPositive, numberOfNegative, total = 0, 0, 0

# Prompts the user to enter an integer.
number = int(input("\nEnter an Integer(press 0 to end): "))

# Indefinite while loop that continues until the user enters 0.
while number != 0:
    if number > 0:
        numberOfPositive += 1  # Increments the numOfPositive variable by 1 whenever the user enters a positive value.
    elif number < 0:
        numberOfNegative += 1  # Increments the numOfNegative variable by 1 whenever the user enters a negative value.
    total += number  # Calculates the total for every input.
    number = int(input("\nEnter an Integer(press 0 to end): "))

# Displays the result.
print(f"\nThe number of positive: {numberOfPositive}\nThe number of negative: {numberOfNegative}"
      f"\nThe sum is: {total}\nThe average is: {total / (numberOfPositive + numberOfNegative):.2f}")
