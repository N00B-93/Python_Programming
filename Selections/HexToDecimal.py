from sys import exit

"""
    This is a program that prompts the user to enter a hex character
    and displays its corresponding decimal integer
"""

# Prompts the user to enter a hex character.
hexDigit = input("\nEnter an hex character(A - F): ")

# Terminates the program if the user enters an invalid character.
if hexDigit < 'A' or hexDigit > 'F':
    print("\nInvalid Character!")
    exit(0)

# Determines the decimal value.
decimalValue = 10 + int(ord(hexDigit) - 65)

# Displays the result.
print(f"\nThe decimal value of '{hexDigit}' is: {decimalValue}")
