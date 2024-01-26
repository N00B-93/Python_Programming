"""
    This is a program that computes the sum of the series give below;

                m(i) = 1/2 + 2/3 + ... + i/i+1
    for i = 1, 2, ... ,20 in tabular form.
"""


def sumOfSeries(limit):
    """
    Calculates the sum of the series i/i+1 from 1 to a given number of terms(limit).

    :param limit: (int) The number of terms to sum.

    :return: (float) The sum of the series up to the given limit(number of terms).
    """
    series = 0

    for i in range(1, limit + 1):
        series += i/(i+1)
    return series


def main():
    print("\ni\t\tm(i)")

    # Displays the result in tabular form.
    for i in range(1, 21):
        print(f"{i}\t\t{sumOfSeries(i):.4f}")


if __name__ == "__main__":
    main()
