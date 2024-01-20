from sys import exit

"""
    This is a program that reads an integer greater than 0 and displays
    all its smallest factors, also known as prime factors.
"""

# Reads in an integer > 0.
number = int(input("\nEnter a integer > 0: "))

if number == 0:  # Stops the program if the user enters 0.
    print("\nInvalid Number, Use an Integer > 0!")
    exit(0)
elif number == 1:  # Display the result if the user input is 1.
    print("\nThe smallest factor is: 1")
elif number == 2:  # Display the result if the user input is 2.
    print("\nThe smallest factors are: 1 2")
elif number == 3:  # Display the result if the user input is 3.
    print("\nThe smallest factors are: 1 3")
else:  # Display the result if the user input is > 3.
    print("\nThe smallest factors are: ", end="")
    for i in range(2, (number // 2) + 1):
        while number % i == 0:
            number = number / i
            print(f"{i} ", end="")
