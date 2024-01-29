from PrimeNumbers import isPrime
from ReverseInteger import reverse


"""
    This is a program that displays the first 100 Emirps, 10 per line.
    An Emirp (prime spelled backward) is a non palindromic prime number whose reversal is also a prime.
"""


def main():
    counter = 2
    number = 2
    lineCounter = 0

    print("The first 100 Emirps are; ")
    while counter <= 100:
        # Displays a number if it's prime, and it's reverse is also prime.
        if isPrime(number) and isPrime(reverse(number)):
            print(f"{number} ", end="")
            lineCounter += 1
            counter += 1
            # Displays a newline if lineCounter is a multiple of 10.
            if lineCounter % 10 == 0:
                print()
        number += 1


if __name__ == "__main__":
    main()
