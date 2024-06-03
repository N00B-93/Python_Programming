"""
    This is a program that prompts the user to enter an  integer and checks whether the number is divisible by
    both 5 and 6, divisible by 5 or 6, or just
    one of them (but not both). 
"""

# Prompts the user to enter an integer.
number = int(input("\nEnter an Integer: "))

# Checks if the number entered is divisible by 5 and 6 and displays the result.
print(f"\nIs {number} divisible by 5 and 6? {number % 5 == 0 and number % 6 == 0}")

# Checks if the number entered is divisible by 5 or 6 and displays the result.
print(f"\nIs {number} divisible by 5 or 6? {number % 5 == 0 or number % 6 == 0}")

# Checks if the number entered is divisible by 5 or 6, but not both.
print(f"\nIs {number} divisible by 5 or 6 but not both? "
      f"{(number % 5 == 0 or number % 6 == 0) and not (number % 5 == 0 and number % 6 == 0)}")
