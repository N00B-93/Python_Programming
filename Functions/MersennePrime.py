def isPrime(n):
    """
    Checks if a number is prime.

    Args:
        n (int): The number to check for primality.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    # Checking for factors from 2 to n//2
    for i in range(2, (n // 2) + 1):
        if n % i == 0:
            return False  # Not prime if divisible by any number other than 1 and itself
    return True  # Prime if not divisible by any number other than 1 and itself


def printMersennePrimes():
    """
    Prints Mersenne primes of the form 2^p - 1.

    Returns:
        None.
    """
    print("\t p\t\t", "2^p - 1")
    print("\t------------------------")
    for i in range(2, 32):  # Checking for primes from 2 to 31 (inclusive)
        if isPrime(i):
            mersennePrime = (pow(2, i) - 1)
            print("\t", i, "\t\t", mersennePrime)


def main():
    """
    Main function to find and display Mersenne primes.
    """
    printMersennePrimes()


if __name__ == "__main__":
    main()
