"""
    A Pentagonal number is a number defined as n(3n - 1)/2.
    This is a program that uses a function with the header;
            getPentagonalNumber(n) for n = 1, 2, 3,...
    to calculate the first 100 pentagonal numbers and then the numbers are displayed them 10 per line.
"""


def getPentagonalNumber(number):
    """
    Returns a pentagonal number.

    :param number: (int) The number whose pentagonal equivalent is to be calculated.

    :return: (int) The pentagonal number
    """

    return number * (3 * number - 1) / 2


def main():
    lineCounter, n = 0, 1

    while n < 100:
        # Prints a pentagonal number followed by a new line.
        print(f"{int(getPentagonalNumber(n))} ", end="")
        n += 1  # Increments n by 1.
        lineCounter += 1  # Increments lineCounter.
        # Displays a newline if lineCounter is a multiple of 10.
        if lineCounter % 10 == 0:
            print()


if __name__ == "__main__":
    main()

