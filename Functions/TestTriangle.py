from MyTriangle import isValid, area

"""
    This is a program that imports the module Triangle and uses the functions present in the module to
    determine whether a triangle is valid and to calculate the area of that triangle if it's valid.
"""


def main():
    # Reads in the sides of the Triangle.
    side1 = float(input("\nEnter the length of side1:"))

    side2 = float(input("\nEnter the length of side2:"))

    side3 = float(input("\nEnter the length of side3:"))

    if isValid(side1, side2, side3):
        print(f"\nThe area of the triangle is {area(side1, side2, side3):.3f}")
    else:
        print("\nThe Triangle is not valid.")


if __name__ == "__main__":
    main()
