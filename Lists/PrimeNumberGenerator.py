"""
    This is a program that prompts the user to enter a number greater than 1 and then generates a list of numbers from 2 to the number entered.
    The program than passes each element in the list to a function;
                def isPrime(number: int) -> bool
    and then loops through the list and displays whether an element is prime or composite(not prime).
"""


def isPrime(number: int) -> bool:
    """
    Checks whether a number is prime or not.

    :param number: (int) The number to be checked.

    :return: (bool) True if the number is prime, else False.
    """
    divisor: int = 2

    while divisor < (number // 2) + 1:
        if number % divisor != 0:
            divisor += 1
            continue
        else:
            return False
    return True


def main() -> None:
    # Prompts the user to enter an integer greater than 1.
    number: int = int(input("\nEnter an integer greater than 1: "))
    
    # Displays an error message and continues to prompt the user to enter a number greater than 1.
    while number <= 1:
        print("\nInvalid input, Try again.")
        number: int = int(input("\nEnter an integer greater than 1: "))

    # Creates an empty list.
    listOfNumbers: list = list()

    # Fills the list with number from 2 to the number entered by the user.
    [listOfNumbers.append(i) for i in range(2, number + 1)]

     # Loops through the list and displays whether an element is prime or not.
    for element in listOfNumbers:
        if isPrime(element):
            print(f"\n{element} is prime.")
        else:
            print(f"\n{element} is composite.")


if __name__ == "__main__":
     main()

