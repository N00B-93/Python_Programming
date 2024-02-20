from Customer import Customer

"""
    This is a program that creates an object of the
    Customer class and prompts the user to enter data for each of the object’s data
    attributes. The data is then stored in the object and displayed on the screen using
    the object's __str__ method.
"""


def main():
    # Prompts the user to enter a name.
    name = input("\nEnter Name: ")

    # Reads in the user's address.
    address = input("\nEnter Address: ")

    # Reads in the user's phone number.
    phoneNumber = input("\nEnter Phone Number: ")

    # Reads in the user's ID.
    customerID = input("\nEnter Customer ID: ")

    # Asks if the user wants to be on the mailing list.
    onMailingList = input("\nDo you want to be on the Mailing List('y' for yes 'n' for no)? ")

    onMailingList = True if onMailingList.lower() == 'y' else False

    customer = Customer(customerID, onMailingList, name, address, phoneNumber)

    print(customer.__str__())


if __name__ == "__main__":
    main()
