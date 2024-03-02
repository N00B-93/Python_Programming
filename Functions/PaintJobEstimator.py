"""
    A painting company has determined that for every 112 square feet of wall space, one gallon 
    of paint and eight hours of labor will be required. The company charges $35.00 per hour for labor. 
    This is a program that asks the user to enter the square feet of wall space to be painted and the price of the paint
     per gallon.
    Then displays the following information:
    • The number of gallons of paint required
    • The hours of labor required
    • The cost of the paint
    • The labor charges
    • The total cost of the paint job
"""


def gallonOfPaintRequired(squareFeetOfWall):
    """
    Returns the number of gallons of paint to be used given a particular wall size.

    :param squareFeetOfWall: (float) The square feet of wall to be painted.

    :return: (float) Number of gallons of paint required.
    """
    return squareFeetOfWall / 112


def hoursOfLabour(squareFeetOfWall):
    """
    Returns the number of hours it takes to paint a given square feet of a wall.

    :param squareFeetOfWall: (float) The square feet of wall to be painted.

    :return: (float) The hours of labour to paint a given wall.
    """
    return squareFeetOfWall / 112 * 8


def costOfPaint(squareFeetOfWall, priceOfPaintPerGallon):
    """
    Returns the amount to paint a given square feet of wall.

    :param squareFeetOfWall: (float) The square feet of wall to be painted.

    :param priceOfPaintPerGallon: (float) The cost of a gallon of paint.

    :return: (float) Total cost to paint a wall of give dimension.
    """
    return gallonOfPaintRequired(squareFeetOfWall) * priceOfPaintPerGallon


def labourCharges(squareFeetOfWall):
    """
    Returns the labour charges to paint a wall of given dimension.

    :param squareFeetOfWall: (float) Size of the wall to be painted.

    :return: (float) Cost of labour to paint a wall of given dimension.
    """
    return hoursOfLabour(squareFeetOfWall) * 35.00


def main() -> None:
    # Reads in the Square feet of wall space to be painted and the price of paint per gallon.
    squareFeetOfWall = eval(input("\nEnter the square feet of wall to be painted: "))
    priceOfPaintPerGallon = eval(input("\nEnter the price of paint per gallon: $ "))

    # Displays the number of gallons of paint required.
    print(f"\nNumber of gallons of Paint required: {gallonOfPaintRequired(squareFeetOfWall):.2f} gallons")

    # Displays the hours of labour required.
    print(f"\nHours of labour required: {hoursOfLabour(squareFeetOfWall):.2f} hours")

    # Displays the cost of paint required.
    print(f"\nCost of Paint: $ {costOfPaint(squareFeetOfWall, priceOfPaintPerGallon):.2f}")

    # Displays the Labour charges.
    print(f"\nThe Labour Charges is: $ {labourCharges(squareFeetOfWall):.2f}")

    # Displays the total cost of the paint job.
    print(f"\nTotal Cost of paint job: $ {labourCharges(squareFeetOfWall) + costOfPaint(squareFeetOfWall,
                                                                                        priceOfPaintPerGallon):.2f}")


if __name__ == "__main__":
    main()
