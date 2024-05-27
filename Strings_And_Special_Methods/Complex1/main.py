from Complex1 import Complex1

"""
    This is a program that tests the functionalities of the Complex1 class.
"""


def main() -> None:
    # Creates two Complex1 Objects.
    c1 = Complex1(3.5, 6.5)
    c2 = Complex1(-3.5, 1.0)

    # Tests all the methods in the Complex1 class
    print()
    print(f"({c1.getRealPart()} + {c1.getImaginaryPart()}i) + ({c2.getRealPart()} + {c2.getImaginaryPart()}i) = "
          f"{c1.__add__(c2).__str__()}")
    print(f"({c1.getRealPart()} + {c1.getImaginaryPart()}i) - ({c2.getRealPart()} + {c2.getImaginaryPart()}i) = "
          f"{c1.__sub__(c2)}")
    print(f"({c1.getRealPart()} + {c1.getImaginaryPart()}i) * ({c2.getRealPart()} + {c2.getImaginaryPart()}i) = "
          f"{c1.__mul__(c2).__str__()}")
    print(f"({c1.getRealPart()} + {c1.getImaginaryPart()}i) / ({c2.getRealPart()} + {c2.getImaginaryPart()}i) = "
          f"{c1.__truediv__(c2).__str__()}")
    print(f"|{c1.getRealPart()} + {c1.getImaginaryPart()}i| = {c1.__abs__()}")


if __name__ == "__main__":
    main()
