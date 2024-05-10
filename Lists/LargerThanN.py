"""
    This is a program that prompts the user to enter a list of numbers and an integer and the displays all the numbers
    in the list that are larger than the integer entered by the user.
"""


def largerThanN(numberList: list, number: int) -> None:
    """
    This displays all the elements of the list that are greater than the number specified.

    :param numberList: (int) The list containing numbers.

    :param number: (int) The number whose counterpart in the list that are greater than it is to be printed.

    :return: None.
    """
    numberList.sort()

    startPoint: int = numberList.index(number)

    if max(numberList) == number:
        print(f"\nNo number is greater than {number}")
        return

    print(f"\nThe numbers greater that {number} in the list are: ", end="")
    for i in range(startPoint + 1, len(numberList)):
        if numberList[i] > number:
            print(f"{numberList[i]} ", end="")


def main() -> None:
    try:
        # Prompts the user to enter a list of numbers.
        numberString: str = input("\nEnter a list of numbers separated by space: ")

        # Prompts the user to enter a number.
        number: int = int(input("\nEnter a number: "))

        # Removes empty spaces in front of and behind the list of numbers.
        numberString = numberString.strip()

        # Converts the String of numbers to a list of integer Strings.
        numberList: list = numberString.split()

        # Converts each element in the list of numbers to an int.
        numberList = list(map(int, numberList))

        # Displays the numbers in the list larger than the number specified by the user.
        largerThanN(numberList, number)
    except Exception as exception:
        print()
        print(exception.__str__())


if __name__ == "__main__":
    main()
