"""
    This is a program that prompts the user to enter a decimal number
    and the displays the decimal number's binary equivalent.
"""

# Reads in a decimal number.
number = int(input("\nEnter a decimal number: "))

if number == 0:
    print(f"\nThe decimal equivalent of {number} is: 0.")
    exit(0)
elif number < 0:
    print("\nInvalid input, Use positive integers only.")
    exit(1)

# Preserves the original decimal number in a temporary variable.
tempVar = number

binaryNumber = ""

while number != 0:
    # Determines the remainder
    remainder = number % 2

    # Constructs a binary number using the remainder.
    binaryNumber += str(remainder)

    # Peels off the last digit.
    number //= 2

# Displays the result
print(f"\nThe binary equivalent of {tempVar} is: {binaryNumber[::-1]}")
