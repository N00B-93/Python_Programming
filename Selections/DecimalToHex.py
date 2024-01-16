from sys import exit

"""
    This is a program that prompts the user to enter a number between from 0 to 15
    and displays the Hexadecimal representation of that number. If the number is not
    in the range of 1 - 15, an error message is displayed and the program is terminated.
"""

# Prompts the user to enter a decimal number from 0 to 15
decimal = int(input("\nEnter a number from 0 - 15: "))

hexValue = ''

# Assigns the decimal value to the hex values variable if the decimal value is in the range 0 - 9.
if 0 <= decimal < 10:
    hexValue = decimal
else:  # Matches a decimal digit to the correct hex value.
    hexValue = chr(ord('A') + (decimal - 10))

if 0 > decimal or decimal > 15:  # Checks if the value entered is in the range 1 - 15
    print("\nInvalid Input, Try Again.")
    exit(0)

# Displays the result.
print(f"\nThe Hex value is: {hexValue}")
