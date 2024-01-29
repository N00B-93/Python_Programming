from math import pow

"""
    This is a program that computes the value of PI using a function with the header;
                def estimatePI(limit)
    which uses the formular;
                PI = 4(1 - 1/3 + 1/5 - 1/7 + 1/9 - 1/11 + ... + (-1 ^(i + 1) / 2i - 1)
    and displays the value of PI for i = 101, 201,  ..., 901.
"""


def estimatePI(limit):
    """
    Computes the value of PI from 1 to a given limit.

    :param limit: (int) The limit of the iteration.

    :return: (float) The estimated value of PI
    """
    PI = 0

    for i in range(1, limit + 1):
        PI += 4 * (pow(-1, i + 1) / (2 * i - 1))
    return PI


def main():
    print("i\t\tm(i)")

    # Estimates the value of PI for each value of i.
    for i in range(101, 902, 100):
        print(f"{i}\t\t{estimatePI(i)}")


if __name__ == "__main__":
    main()
