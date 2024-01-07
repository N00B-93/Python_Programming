"""
    This is a program that prompts the user to enter three integers
    and displays them in increasing order
"""
# Prompts the user to enter the three integers to be sorted.
number1, number2, number3 = eval(input("\nEnter three integers separated by comma: "))

# Sorts the numbers and displays the result.
if number1 <= number2 <= number3:
    print(f"\nThe sorted numbers are {number1}, {number2}, {number3}")
elif number1 <= number3 <= number2:
    print(f"\nThe sorted numbers are {number1}, {number3}, {number2}")
elif number2 <= number3 <= number1:
    print(f"\nThe sorted numbers are {number2}, {number3}, {number1}")
elif number2 <= number1 <= number3:
    print(f"\nThe sorted numbers are {number2}, {number1}, {number3}")
elif number3 <= number2 <= number1:
    print(f"\nThe sorted numbers are {number3}, {number2}, {number1}")
elif number3 <= number1 <= number2:
    print(f"\nThe sorted numbers are {number3}, {number1}, {number2}")
