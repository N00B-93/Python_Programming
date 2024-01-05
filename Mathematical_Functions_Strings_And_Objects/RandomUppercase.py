from time import time

"""
    This is a  program that displays a random uppercase letter
    using the time.time() function.
"""
# Generates a random uppercase letter.
asciiValue = 65 + (int(time()) % 26)

# Displays the result.
print(f"\nThe random uppercase letter is: '{chr(asciiValue)}'")