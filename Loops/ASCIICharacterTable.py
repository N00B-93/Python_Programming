"""
    This is a program that displays the characters
    in the ASCII character table from ! to ~. Ten characters are displayed per line. The characters
    are separated by exactly one space.
"""

# Initializes the counter variable to 0.
counter = 0

for character in range(ord('!'), ord('~')):
    # Prints the ASCII Characters from '!' to '~'
    print(f"{chr(character)} ", end="")
    counter += 1  # Increments the counter by 1

    # Prints a newline if the counter is a multiple of 10.
    if counter % 10 == 0:
        print()
