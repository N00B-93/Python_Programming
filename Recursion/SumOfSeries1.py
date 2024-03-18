"""
    This program uses a recursive method with the header;
                public static double recursiveSumOfSeries(int numberOfTerms)
    to return the sum of the first n terms of the series i / (i + 1) for n = 1, 2, 3, ..., 20.
"""


def recursiveSumOfSeries(numberOfTerms: int) -> float:
    """
    This returns the sum of the first n terms of the series i / (i + 1) for any integer n >= 1 recursively.
    :param numberOfTerms:(int) The number of terms.
    :return: (float) The sum of the first n terms.
    """
    if numberOfTerms == 1:
        return 0.5
    return (numberOfTerms / (numberOfTerms + 1)) + recursiveSumOfSeries(numberOfTerms - 1)


def main() -> None:
    print("i\t\tm(i)")
    print("-----------------")
    for i in range(1, 21):
        # Displays the sum of the series for i = 1, 2, 3, ..., 20
        print(f"{i}\t\t{recursiveSumOfSeries(i):.4f}")


if __name__ == "__main__":
    main()
