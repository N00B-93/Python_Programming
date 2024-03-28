class Location:
    """
    A class that represents a Location.

        Attributes:

            maxValue: (float) The maximum value in a 2-D list.

            row: (int) The row number of the maxValue.

            col: (int) The column number of the maxValue.
    """
    def __init__(self, row=0, col=0, maxValue=0.0):
        self.row = row
        self.col = col
        self.maxValue = maxValue

    def locateLargest(self, myList: list):
        """
        This returns the maximum element of a 2-D list and the row and column where it can be found.

        :param myList: (list) The list whose maxValue and position of max value is to be determined.

        :return: (Location) A location object initialized with the list's max value, and it's location.
        """
        maxValue = myList[0][0]
        row, col = 0, 0

        for i in range(len(myList)):
            for j in range(len(myList)):
                if myList[i][j] > maxValue:
                    maxValue = myList[i][j]
                    row, col = i, j

        return Location(row, col, maxValue)


def main() -> None:
    myList, i = [], 0
    # Reads in element of a 2-D list(3x3 matrix).
    while len(myList) < 3:
        numberList: list = input(f"\nEnter three elements of row {i} separated by space: ").split()
        
        # Displays an error message if the user input is not 3 number separated by space.
        if not len(numberList) == 3:
            print("Invalid input, Use 3 numbers separated by space")
            continue

        # Converts the element of each 1-D list to integer and appends the list to a new list.
        myList.append(list(map(int, numberList)))

        i += 1
    
    # Creates a Location Object.
    location = Location()
    
    # Determines the largest element in the list, and it's location.
    location = location.locateLargest(myList)
    
    # Displays the result.
    print(f"\nThe maximum value is: {location.maxValue} and is located at {(location.row, location.col)}")


if __name__ == "__main__":
    main()
