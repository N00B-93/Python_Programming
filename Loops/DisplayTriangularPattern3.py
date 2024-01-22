"""
    This program displays the triangular pattern:
                     1
                   2 1
                 3 2 1
               4 3 2 1
             5 4 3 2 1
           6 5 4 3 2 1
    in the console.
"""

space = 6

print()
for i in range(7):
    for j in range(space):
        print("  ", end="")
    for k in range(i, 0, -1):
        print(f"{k} ", end="")
    space -= 1
    print()
