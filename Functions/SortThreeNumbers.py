"""
    This is a program that uses a function with the header;
                def displaySortedNumbers(num1, num2, num3)
    to sort and display three numbers entered by the user in ascending order.
"""

def displaySortedNumbers(num1, num2, num3):
    """
    Displays three numbers sorted in ascending order.

    :param num1: (float) The first number.

    :param num2: (float) The second number.

    :param num3: (float) The third number.

    :return: None.
    """
    if num3 <= num2 and num2 <= num1:
        print(f"\nThe sorted numbers are: {num3, num2, num1}")
    elif num3 <= num1 and num1 <= num2:
        print(f"\nThe sorted numbers are: {num3, num1, num2}")
    elif num2 <= num3 and num3 <= num1:
        print(f"\nThe sorted numbers are: {num2, num3, num1}")
    elif num2 <= num1 and num1 <= num3:
        print(f"\nThe sorted numbers are: {num2, num1, num3}")
    elif num1 <= num2 and num2 <= num3:
        print(f"\nThe sorted numbers are: {num1, num2, num3}")
    elif num1 <= num3 and num3 <= num2:
        print(f"\nThe sorted numbers are: {num1, num3, num2}")

    return

        

def main():
    # Reads in the three numbers to be sorted.
    number1 = float(input("\nEnter the first number: "))
    number2 = float(input("\nEnter the second number: "))
    number3 = float(input("\nEnter the third number: "))
    
    # Displays the numbers sorted in ascending order.
    displaySortedNumbers(number1, number2, number3)


if __name__ == "__main__":
    main()

