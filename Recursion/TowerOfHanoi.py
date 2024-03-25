"""
    This is a program that prompts the user to enter number of disks and then solves the Tower of Hanoi
    problem for that number of disks using recursion.
"""


def towerOfHanoi(numberOfDisks: int, srcRod: int, auxRod: int, destRod: int) -> None:
    """
    This solves the Tower of Hanoi puzzle recursively.
    :param numberOfDisks: (int) The number of disks to be moved.

    :param srcRod: (int) The source rod from which the disks are moved.

    :param auxRod: (int) The auxiliary rod used for intermediate moves.

    :param destRod: (int) The destination rod to which the disks are moved.
    """
    if numberOfDisks > 0:
        towerOfHanoi(numberOfDisks - 1, srcRod, destRod, auxRod)
        print(f"\nMove disk {numberOfDisks} from Rod {srcRod} to Rod {destRod}")
        towerOfHanoi(numberOfDisks - 1, auxRod, srcRod, destRod)


def main() -> None:
    while True:
        try:
            # Prompts the user to enter the number of disks.
            numberOfDisks = int(input("\nEnter the number of disks: "))
            
            # Informs the user to enter a valid number of disks if the number of disks entered is <= 0.
            if numberOfDisks <= 0:
                print("\nInvalid input, Use a number of disk >= 0.")
                continue
            
            # Display the solution to the Tower of Hanoi puzzle.
            towerOfHanoi(numberOfDisks, 1, 2, 3)
            break
        except ValueError:
            print("\nInvalid input, Try again.")


if __name__ == "__main__":
    main()
