"""
    This is a program that determines the number of prime numbers less than 10000
    using a function with the header;
                def isPrime(number)
"""


def isPrime(number):
    """
    Checks if a number is prime or not.

    :param number: (int) The number to be checked.

    :return: (bool) True if number is prime and False otherwise.
    """
    divisor = 2

    while divisor < number / 2:
        if number % divisor == 0:
            return False
        divisor += 1
    return True


def main():
    # Initializes the prime number counter to 0.
    primeCounter = 0

    # Checks if a number is prime.
    for i in range(2, 10000):
        if isPrime(i):
            primeCounter += 1

    # Displays the result.
    print(f"\nThe number of prime numbers less than 10000 is {primeCounter}")


if __name__ == "__main__":
    main()
