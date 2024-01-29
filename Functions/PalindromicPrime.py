from PalindromeInteger import reverse
from PrimeNumbers import isPrime

"""
    This is a program that displays the first 100 Palindromic Prime numbers.
    A Prime number is a palindromic prime number if it is equal to it's reverse.
"""


def main():
    counter = 0
    number = 2
    lineCounter = 0

    print("\nThe first 100 Palindromic Primes are; ")

    while counter != 100:
        # Displays a number if its prime and a palindrome
        if isPrime(number) and number == reverse(number):
            print(f"{number} ", end="")
            counter += 1
            lineCounter += 1
            # Displays a newline if the lineCounter is a multiple of 10.
            if lineCounter % 10 == 0:
                print()
        number += 1


if __name__ == "__main__":
    main()
