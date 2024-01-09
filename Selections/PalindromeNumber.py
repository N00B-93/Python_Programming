from sys import exit

"""
    This is a program that prompts the user to enter a three-digit
    integer and determines whether it is a palindrome number.
    A number is a palindrome if it reads the same from right to left and from left to right.
"""

# Prompts the user to enter a 3-digit number.
number = int(input("\nEnter a 3-digit number: "))

# Terminates the program if the number entered by the user is not a 3-digit number.
if number < 100 or number > 999:
    print("\nInvalid Input, Enter a 3-digit number")
    exit(0)

# Peels off each digit in the number.
firstDigit = number // 100
secondDigit = (number // 10) % 10
lastDigit = number % 10

# Reverses the number
reversedNumber = lastDigit * 100 + secondDigit * 10 + firstDigit

# Display whether the number is a palindrome or not.
if reversedNumber == number:
    print(f"\n{number} is a palindrome")
else:
    print(f"\n{number} is not a palindrome")
