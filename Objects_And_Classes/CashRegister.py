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

    # Creates a list of items.
    itemList = [item1, item2, item3]

    # Creates a CashRegister Object.
    cashRegister = CashRegister(itemList)


if __name__ == "__main__":
    main()

