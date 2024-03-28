"""
    This is a program that prompts the user to enter a decimal number and then displays the hexadecimal
    equivalent of the user's input.
"""


# Prompts the user to enter an integer.
decimal = int(input("\nEnter an integer: "))

# Displays 0 if user input is 0.
if decimal == 0:
    print(f"\nThe hexadecimal equivalent of {decimal} is: {decimal}")
    exit(0)
elif decimal < 0:  # Displays an error message if user input is less than 0.
    print("\nInvalid input, Use positive integers only.")
    exit(1)

hexNumber, tempVar = "", decimal

while decimal > 0:
    remainder = decimal % 16
    if remainder < 10:
        hexNumber += str(remainder)
    else:
        hexNumber += chr((remainder - 10) + ord("A"))
    decimal //= 16

# Displays the result.
print(f"\nThe hexadecimal equivalent of {tempVar} is: {hexNumber[::-1]}")
