"""
    This is a program that uses a function with the header;
                def sort(points)
    to sort the list of points shown below based on their y-coordinates;
                [[4, 34], [1, 7.5], [4, 8.5], [1, -4.5], [1, 4.5], [4, 6.6]] 
"""


def sort(points):
    """
    Sorts a 2-Dimensional list containing points based on the y-coordinatesof the points.

    :param points: (list) The 2-Dimensional list containing the points to be sorted.

    :return: None.
    """
    for passes in range(len(points)):
        for row in range(1, len(points)):
            if points[row - 1][1] > points[row][1]:
                points[row], points[row - 1] = points[row - 1], points[row]


def main():
    # List of points to be sorted.
    points = [[4, 34], [1, 7.5], [4, 8.5], [1, -4.5], [1, 4.5], [4, 6.6]]

    # Displays the points before sorting.
    print("\nPoints before sorting.")
    [[print(f"{points[row][col]} ", end="") for col in range(len(points[row]))] and print() or row for row in range(len(points))]
    
    # Sorts the points based on their y-coordinates.
    sort(points)

    # Displays the points before sorting.
    print("\nPoints after sorting.")
    [[print(f"{points[row][col]} ", end="") for col in range(len(points[row]))] and print () or row for row in range(len(points))]


if __name__ == "__main__":
      main()

