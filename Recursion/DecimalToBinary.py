"""
    This is a program that prompts the user to enter a positive integer and then displays the binary equivalent
    of the number as a String using a recursive function.
"""


def decimalToBinary(number: int) -> str:
    if number == 0:
        return "0"
    elif number == 1:
        return "1"
    return str(number % 2) + decimalToBinary(number // 2)


def main() -> None:
    while True:
        try:
            # Prompts the user to enter a positive integer.
            decimal = int(input("\nEnter a positive integer: "))

            # Continues to loop till the user enters a number greater than or equal to 0.
            while decimal < 0:
                print("\nInvalid input. Try again.")
                decimal = int(input("\nEnter a positive integer: "))
            print(f"\nThe binary equivalent of {decimal} is: {decimalToBinary(decimal)}")
            break
        except ValueError:
            print("\nInvalid input. Try again.")


if __name__ == "__main__":
    main()
