def isPrime(n):
    """
    Checks if a number is prime or not.

    Args:
        n (int): The number to be checked for primality.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    # Checking divisibility from 2 to n//2
    for i in range(2, (n // 2) + 1):
        if n % i == 0:
            return False  # If divisible by any number other than 1 and itself, not prime
    return True  # If not divisible by any number other than 1 and itself, prime


def printTwinPrimes():
    """
    Prints twin primes less than 1000.
    """
    twin = 2  # Initialize the first twin prime
    print("\nThe twin primes less than 1000 are:")
    for i in range(3, 1001):
        if isPrime(i):
            if i - twin == 2:
                print("(", twin, ", ", i, ")", sep="")
            twin = i  # Update the twin prime for the next iteration


def main():
    """
    Main function to find and display twin primes less than 1000.
    """
    printTwinPrimes()


if __name__ == "__main__":
    main()

