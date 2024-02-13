"""
    This is a program that finds the two nearest points
    in a 3-Dimensional space given a list of 3-dimensional points.
"""


def distance(x1, x2, y1, y2, z1, z2):
    """
    Calculates the distance between two 3-dimensional points.

    :param x1: (float) The x-coordinate of the first point.

    :param x2: (float) The x-coordinate of the second point.

    :param y1: (float) The y coordinate of the first point.

    :param y2: (float) The y coordinate of the second point.

    :param z1: (float) The z-coordinate of the first point.

    :param z2: (float) The z-coordinate of the second point.

    :return: (float) The distance between two 3-dimensional points.
    """
    return ((x2 - x1)**2 + (y2 - y1)**2) + (z2 - z1)**2


def nearestPoints(points):
    """
    Finds the two nearest points in a list of 3-dimensional points.

    :param points: (list) A list of 3-dimensional.

    :return: (int) The indices of the two nearest points in the list containing points.
    """
    p1, p2 = 0, 1

    smallestDistance = distance(points[p1][0], points[p1][1], points[p1][2], points[p2][0], points[p2][1],
                                points[p2][2])

    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            length = distance(points[i][0], points[i][1], points[i][2], points[j][0], points[j][1], points[j][2])

            if length < smallestDistance:
                smallestDistance = length
                p1, p2 = i, j
    return p1, p2


def main():
    # Creates a nested list of 3-D points.
    points = [
                [-1, 0, 3], [-1, -1, -1], [4, 1, 1],
                [2, 0.5, 9], [3.5, 2, -1], [3, 1.5, 3], [-1.5, 4, 2],
                [5.5, 4, -0.5]
    ]

    # Finds the two nearest points.
    idx1, idx2 = nearestPoints(points)

    # Displays the result.
    print("\nThe two nearest points are: ", end="")
    print(f"({points[idx1][0]}, {points[idx1][1]}), ({points[idx2][0]}, {points[idx2][1]})")


if __name__ == "__main__":
    main()
