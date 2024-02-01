class Stock:
    """
    A class representing a stock.

    Attributes:
        name (str): The name of the stock.

        symbol (str): The symbol of the stock.

        previousClosingPrice (float): The previous closing price of the stock.

        newCurrentPrice (float): The current stock price.
    """
    def __init__(self, name, symbol, previousClosingPrice, newCurrentPrice):
        self.__name = name
        self.__symbol = symbol
        self.__previousClosingPrice = previousClosingPrice
        self.__newCurrentPrice = newCurrentPrice

    def getName(self):
        """
        Returns the name of the stock.

        :return: (str) The name of the stock,
        """
        return self.__name

    def getSymbol(self):
        """
        Returns the symbol of the stock.

        :return: (str) The symbol of the stock.
        """
        return self.__symbol

    def setPreviousClosingPrice(self, previousClosingPrice):
        """
        Sets the previous closing price of the stock.

        :param previousClosingPrice: (float) The previous closing price of the stock

        :return: None
        """
        self.__previousClosingPrice = previousClosingPrice

    def getPreviousClosingPrice(self):
        """
        Returns the previous closing price of the stock.

        :return: (float) The previous closing price of the stock.
        """
        return self.__previousClosingPrice

    def setNewCurrentPrice(self, newCurrentPrice):
        """
        Sets the new current price of the stock.

        :param newCurrentPrice: (float) The new current price of the stock.

        :return: None.
        """
        self.__newCurrentPrice = newCurrentPrice

    def getNewCurrentPrice(self):
        """
        Returns the new current price of the stock.

        :return: (float) The new current price of the stock.
        """
        return self.__newCurrentPrice

    def getChangePercent(self):
        """
        Returns the price change percentage of the stock.

        :return: (float) The percentage price change of the stock.
        """
        return ((self.__previousClosingPrice - self.__newCurrentPrice) / 100) * 100


def main():
    # Creates a Stock Object.
    stock = Stock("Intel Corporation", "INTC", 20.5, 20.35)

    print("\nStock Details:")

    # Displays the properties of the stock.
    print(f"Name: {stock.getName()}\nSymbol: {stock.getSymbol()}\nPrevious Closing Price: "
          f"{stock.getPreviousClosingPrice()}\nNew Current Price: {stock.getNewCurrentPrice()}\n"
          f"Price Change Percentage: {format(stock.getChangePercent(), '.2f')}")


if __name__ == "__main__":
    main()
