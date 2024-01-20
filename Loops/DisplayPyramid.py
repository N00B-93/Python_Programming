from sys import exit


"""
    This is a program that prompts the user to enter an integer
    from 1 to 15 and displays a pyramid, as shown below:

                    1
                 2  1  2
              3  2  1  2  3
            4  3  2 1  2  3  4
         5  4  3  2 1  2  3  4  5
      6  5  4  3  2 1  2  3  4  5  6
   7  6  5  4  3  2 1  2  3  4  5  6  7
"""
# Reads in a number.
number = int(input("\nEnter a number from 1 - 15: "))

if number <= 1 or number > 15:
    print("\nInvalid number, enter a number > 1 and <= 15")
    exit(0)

# Assigns the space variable to the value of the number entered.
space = number

for i in range(1, number + 1):
    # Prints space - 1 spaces before the first entry of each line.
    for m in range(space, 1, -1):
        print("  ", end="")

    # Prints the first half of the pyramid.
    for j in range(i, 0, -1):
        print(f"{j} ", end='')

    # Prints the second half of the pyramid if i >= 2.
    if i >= 2:
        for k in range(2, i + 1):
            print(f"{k} ", end='')

    space -= 1  # Reduces the space variable by 1 before the next iteration of the outer loop.
    print()  # Prints a new line after each line.
