from ProductionWorker import ProductionWorker

"""
    This is a program that creates an object of the
    ProductionWorker class and prompts the user to enter data for each of the object’s data
    attributes. The data is then stored in the object and displayed on the screen using
    the object's __str__ method.
"""


def main():
    # Prompts the user to enter the Production Worker's name.
    name = input("\nEnter Name: ")

    # Prompts the user to enter Employee ID.
    employeeID = input("\nEnter Employee ID: ")

    # Prompts the user to enter Shift.
    shift = int(input("\nEnter Shift('1' for day, '2' for night): "))

    # Prompts the user to enter Hour pay rate.
    hourlyRate = float(input("\nEnter Hourly Rate: $ "))

    productionWorker = ProductionWorker(shift, hourlyRate, name, employeeID)

    print("\nEmployee Details: ")
    print(productionWorker.__str__())


if __name__ == "__main__":
    main()
