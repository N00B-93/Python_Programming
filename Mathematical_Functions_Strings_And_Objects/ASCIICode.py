"""
    This is a program that receives an ASCII
    code (an integer between 0 and 127) and displays its character.
"""

# Reads in an ASCII code between 0 and 127
asciiValue = int(input("\nEnter an ASCII code between 0 and 127: "))

# Displays the result.
print(f"\nThe character is '{chr(asciiValue)}'")
