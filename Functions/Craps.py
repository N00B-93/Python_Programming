from random import randint
from sys import exit

"""
    This program simulates the game of craps.
"""


def roll():
    """
    This is a function that generates two random numbers between 1 and 6 and returns their sum to the caller.

    Returns:
        - total(int): Sum of two random numbers generated by the function.
    """

    a = randint(1, 6)
    b = randint(1, 6)

    return a + b


def main():
    """
    The main function.
    """

    choice = input('\nEnter "y" to roll dice: ')

    # Continues the game if choice is 'y' or and terminates the game otherwise.
    if choice == 'y':
        pass
    else:
        exit(0)

    # Rolls the dice.
    point = roll()

    # Checks if player wins or loses on the first roll.
    if point == 2 or point == 3 or point == 12:
        print("\nYour rolled ", point, "\nYou LOSE!!!", sep="")
        exit(0)
    elif point == 7 or point == 11:
        print("\nYou rolled ", point, "\nYou WIN!!!", sep="")
        exit(0)
    else:
        print("\nYour point is:", point)

    newPoint = 0

    # Continues to roll the dice till user plays his/her point or the roll is 7.
    while newPoint != point:
        choice = input("\nEnter 'y' to roll dice: ")
        if choice == 'y':
            pass
        else:
            exit(0)

        newPoint = roll()

        if newPoint == 7:
            print("You rolled ", newPoint, "\nYou LOSE!!!")
            break
        elif point == newPoint:
            print("\nYou rolled ", point, "\nYou WIN!!!")
            break
        else:
            print("\nYou played", newPoint)


if __name__ == "__main__":
    main()
