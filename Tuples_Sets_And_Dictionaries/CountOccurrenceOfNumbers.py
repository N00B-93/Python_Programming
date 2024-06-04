"""
    This is a program that reads an unspecified number of integers and finds the ones that have the
    most occurrence.
"""


def main() -> None:
    try:
        # Prompts the user to enter a list of numbers.
        numberList = input("\nEnter a list of numbers: ").split()

        numberList = [int(number) for number in numberList]
    except ValueError:
        print("\nError: Please use only integers separated by space, try again.")
        exit(1)

    # Dictionary to hold each digit, and it's number of occurrence.
    numberAndOccurrence: dict = {}

    # Determines the number of occurrence of each digit.
    for number in numberList:
        if number not in numberAndOccurrence.keys():
            occurrence = numberList.count(number)
            numberAndOccurrence.update({number: occurrence})

    # Displays the Occurrence of each digit.
    print("\nThe Occurrence of each digit is: ")
    var = {print(f"{key} occurs {value} time.") if value == 1 else print(f"{key} occurs {value} times.") for key, value
           in numberAndOccurrence.items()}

    # Determines the maximum occurrence.
    maximumOccurrence: int = max(numberAndOccurrence.values())

    # Displays the number(s) with the maximum occurrence.
    print("\nThe number(s) with maximum occurrence: ", end='')
    [print(f"{number} ", end='') or number for number in numberAndOccurrence.keys() if
     numberAndOccurrence.get(number) == maximumOccurrence]


if __name__ == "__main__":
    main()
