from random import randint


"""
    The bean machine, also known as a quincunx or the Galton box, is a device for statistics experiments named after 
    English scientist Sir Francis Galton. It consists of an upright board with evenly spaced nails (or pegs) in a 
    triangular pattern.
    Balls are dropped from the opening of the board. Every time a ball hits a nail,
    it has a 50% chance of falling to the left or to the right. The piles of balls are
    accumulated in the slots at the bottom of the board.
    This is a program that simulates the bean machine, the user is prompted to enter the number of balls and slots and 
    the ball path as it falls is displayed.
"""


def generatePath(numberOfSlots):
    """
    Generates a path for a ball given the number of slots.

    :param numberOfSlots: (int) The number of slots.

    :return path: (list) The generated path.
    """
    direction = ['L', 'R']

    path = numberOfSlots * [" "]

    for i in range(len(path)):
        n = randint(0, 1)

        path[i] = direction[n]

    return path


def printBallPath(path):
    """
    Prints the path of a falling ball.

    :param path: (list) The path of the ball.

    :return: None.
    """
    print("".join(path), end="", sep="")


def insertBallsIntoSlots(balls, numberOfSlots):
    """
    Inserts a given amount of balls into a given number of slots.

    :param numberOfSlots: (int) The number of slots.

    :param balls: (int) The number of balls to be inserted.

    :return ballSlot, ballSameSlot: (list) A list containing a ball in a single slot and a list
    containing multiple balls in one slot.
    """
    ballSlot = numberOfSlots * [" "]
    ballInSameSlot = []
    ballIndex = []

    for i in range(balls):
        path = generatePath(numberOfSlots)
        printBallPath(path)
        print()

        countOfBallsInRightPath = path.count('R')

        if countOfBallsInRightPath not in ballIndex:
            ballSlot[countOfBallsInRightPath] = 0
            ballIndex.append(countOfBallsInRightPath)
        else:
            ballInSameSlot.append(countOfBallsInRightPath)
    return ballSlot, ballInSameSlot


def printBalls(tray):
    """
    Prints the balls in a given list(tray).

    :param tray: (list) The list(tray) to be printed.

    :return: None.
    """
    for i in range(len(tray)):
        print(tray[i], "", end="", sep="")
    # print("".join(tray))


def printBallsInSameSlot(index, numberOfSlots):
    """
    Prints the balls in the same slot.

    :param index: (int) The index of the ball.

    :param numberOfSlots: (int) The numberOfSlots.

    :return: None.
    """
    ballTray = numberOfSlots * [" "]
    ballTray[index] = 0

    for i in range(len(ballTray)):
        print(ballTray[i], "", end="", sep="")


def main():
    # Prompts the user to enter the number of balls.
    balls = eval(input("\nEnter the number of balls: "))
    
    # Prompts the user to enter the number of slots.
    numberOfSlots = eval(input("\nEnter the number of slots: "))

    print()
    
    # Inserts the balls into slots.
    ballSlot, ballInSameSlot = insertBallsIntoSlots(balls, numberOfSlots)

    print("\n")
    
    # Displays balls in the same slot.
    for i in range(len(ballInSameSlot)):
        printBallsInSameSlot(ballInSameSlot[i], numberOfSlots)
        print()
    
    # Displays balls in different slots.
    printBalls(ballSlot)

    print()


if __name__ == "__main__":
    main()
