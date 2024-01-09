from random import randint

"""
    This is a program that generates a 3-digit numb er      and prompts the user to enter a three-digit number      and determines whether the user wins the lottery        according to the following rules:
        1. If the user input matches the lottery number         in the exact order, the award is $10,000.
        2. If all the digits in the user input match al         l the digits in the lottery number, the award       is $3,000.
        3. If one digit in the user input matches a dig         it in the lottery number, the award is $1,000."""

# Generates a 3-digit number.
lotteryNumber = randint(100, 999)

# prompts the user to enter a 3-digit number.
userGuess = int(input("\nEnter a 3-digit number: "))

# Peels off the digits in the user's input.
firstDigit = userGuess // 100
secondDigit = (userGuess // 10) % 10
lastDigit = userGuess % 10


if lotteryNumber == userGuess:
    print(f"\nExact Match!\nYou've won $ 10, 000!")

