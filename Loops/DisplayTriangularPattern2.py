"""
    This program displays the following Triangular Pattern:
                1 2 3 4 5 6
                1 2 3 4 5
                1 2 3 4
                1 2 3
                1 2
                1
    in the console.
"""

print()
for i in range(6, 0, -1):
    for j in range(1, i + 1):
        print(f"{j} ", end="")
    print()
