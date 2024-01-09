from random import randint

"""
    This is a program that generates a 3-digit number and prompts the user to enter a three-digit number and determines
    whether the user wins the lottery according to the following rules:
        1. If the user input matches the lottery number in the exact order, the award is $10,000.
        2. If all the digits in the user input match all the digits in the lottery number, the award is $3,000.
        3. If one digit in the user input matches a digit in the lottery number, the award is $1,000.
"""

# Generates a 3-digit number.
lotteryNumber = randint(100, 999)

# prompts the user to enter a 3-digit number.
userGuess = int(input("\nEnter a 3-digit number: "))

# Peels off the digits in the user's input.
firstDigit = userGuess // 100
secondDigit = (userGuess // 10) % 10
lastDigit = userGuess % 10

# Peels off the digits in the lottery number
firstLotteryDigit = lotteryNumber // 100
secondLotteryDigit = (lotteryNumber // 10) % 10
lastLotteryDigit = lotteryNumber % 10

# Displays the lottery number and the user's guess.
print(f"\nThe lottery number is {lotteryNumber}\n\nYou played {userGuess}")

if lotteryNumber == userGuess:  # Checks if the user's guess is an exact match.
    print(f"\nExact Match!\nYou've won $ 10, 000!")
# Checks if each number in the user's guess matches all numbers in the lottery number.
elif ((firstDigit == firstLotteryDigit or firstDigit == secondLotteryDigit or firstDigit == lastLotteryDigit) and
      (secondDigit == firstLotteryDigit or secondDigit == secondLotteryDigit or secondDigit == lastLotteryDigit) and
      (lastDigit == firstLotteryDigit or lastDigit == secondLotteryDigit or lastDigit == lastLotteryDigit)):
    print(f"\nYou Match all digits!\nYou've won $ 3, 000")
# Checks if one number in the user's guess matches a number in the lottery number.
elif ((firstDigit == firstLotteryDigit or firstDigit == secondLotteryDigit or firstDigit == lastLotteryDigit) or
      (secondDigit == firstLotteryDigit or secondDigit == secondLotteryDigit or secondDigit == lastLotteryDigit) or
      (lastDigit == firstLotteryDigit or lastDigit == secondLotteryDigit or lastDigit == lastLotteryDigit)):
    print(f"\nYou Match one digit!\nYou've won $ 1, 000")
else:
    print("\nYou win $ 0.00 (:")

