from RetailItem import RetailItem


class CashRegister:
    """
    A class representing a Cash Register Object.

    Attributes:
        
        purchasedItems (list): A list containing RetailItem Objects.
    """
    def __init__(self, purchasedItems = []):
        self.purchasedItems = purchasedItems

    def purchaseItem(self, retailItem):
        """
        Adds a RetailItem Object to the purchasedItems list 

        :param retailItem: (RetailItem) The Object to be added to the list.

        :return: (None).
        """
        self.purchasedItems.append(retailItem)

    def getTotal(self):
        """
        Returns the total price of all retail item in the purchasedItem list.

        :return: (float) Total price of a retail items.
        """
        total = 0

        for item in purchasedItems:
            total += item.getPrice()

        return total

    def clearCart(self):
        """
        Clears the purchasedItems list.

        :return: (None)
        """
        self.purchasedItems.clear()

    
    def showItems(self, retailItem):
        """
        Shows information about a retail item in the purchasedItems list.

        :param retailItem: (RetailItem) The item whose information is to be displayed.

        :return: (str) Information about the retailItem.
        """
        return f"\nDescription: {retailItem.getDescription()}\nUnits In Inventory: {retailItem.getUnitsInInventory()}\nPrice: {retailItem.getPrice()}"


def main():
    # Creates three RetailItem Objects.
    item1 = RetailItem("Faded Jean", 45, 21.25)
    item2 = RetailItem("Hoodie", 52, 35.21)

    item3 = RetailItem("Leather Jacket", 11, 45.60)

    item4 = RetailItem("Baseball Cap", 10, 9.12)

    item5 = RetailItem("Nike Air Jordan", 8, 101.28)

    # Creates a list to represent an empty cart.
    cart = []
    
    choice = ""

    while choice != '0':
        print("\n\t\tAvailable Items")
        
        print(f"1. {item1.getDescription()}\n2. {item2.getDescription()}\n3. {item3.getDescription()}\n4. {item4.getDescription()}\n5. {item5.getDescription()}")
        choice = input("\nEnter choice(press 0 to quit): ")

        match choice:
            case '1':
                cart.append(item1)
            case '2':
                cart.append(item2)
            case '3':
                cart.append(item3)
            case '4':
                cart.append(item4)
            case '5':
                cart.append(item5)
            case _:
                print("\nInvalid option!")
    
    # Creates a CashRegister Object.
    cashRegister = CashRegister(cart)

    # Displays the items in the cart.
    print("\n\t\tItems in Cart:")
    print("\nItem Name\t\t\tQty")
    for items in cart:
        print(f"\n{items.getDescription()}\t\t\t{cart.count(items)}")
    
    # Displays the total price of all items in the cart.
    total = 0

    for item in cart:
        total += item.getPrice()

    print(f"\nThe total price of all items in the cart is: $ {total:.2f}")


if __name__ == "__main__":
    main()

