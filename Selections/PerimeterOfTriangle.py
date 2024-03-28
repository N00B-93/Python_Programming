"""
    This is a program that reads three edges for a triangle and computes the perimeter if the input is valid. 
    Otherwise, display that the input is invalid. The input is valid if the sum of every pair of two edges is greater
    than the remaining edge.
"""


def main():
    # Prompts the user to enter the three sides of a Triangle.
    side1 = float(input("\nEnter the length of the first side: "))
    side2 = float(input("\nEnter the length of the second side: "))
    side3 = float(input("\nEnter the length of the third side: "))

    # Displays the perimeter if the length of every pair of two side is greater than the remaining side.
    if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
        print(f"\nThe perimeter is: {(side1 + side2 + side3):.2f}")
    # Displays an error message if the length of one side is greater than thw other two.
    elif side1 > side2 + side3 or side2 > side1 + side3 or side3 > side1 + side2:
        print("\nThe input is invalid, The length of one side must not be greater than the other two.")


if __name__ == "__main__":
    main()
