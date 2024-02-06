from sys import exit

"""
    This program that creates an Account object with an account id of 1122, a
    balance of $20,000, and an annual interest rate of 4.5%. $2,500 is withdrawn from the account and $ 3,000 
    was deposited to the account. The id, balance, monthly interest rate, and monthly interest is then displayed.
"""


class Account:
    """
    class representing an Account.

    Attributes:
        ID (int): the id of the account.

        balance (float): the balance of the account.

        annualInterestRate (float): the annual interest rate of the account.
    """

    def __init__(self, ID=0, balance=100.0, annualInterestRate=0.0):
        self.__ID = ID
        self.__balance = balance
        self.__annualInterestRate = annualInterestRate

    def getID(self):
        """
        Returns the id of the account.

        :return: (int) The id of the account.
        """
        return self.__ID

    def setID(self, value):
        """
        Sets the id of the account to a given value.

        :param value: (int) The id to set.

        :return: None.
        """
        self.__ID = value

    def getBalance(self):
        """
        Returns the balance of the account.

        :return: (float) The balance of the account.
        """
        return self.__balance

    def setBalance(self, value):
        """
        Sets the balance of the account to a given value.

        :param value: (float) The balance to set.

        :return: None.
        """
        self.__balance = value

    def getAnnualInterestRate(self):
        """
        Returns the annual interest rate of the account.

        :return: (float) The annual interest rate of the account.
        """
        return self.__annualInterestRate

    def setAnnualInterestRate(self, value):
        """
        Sets the annual interest rate of the account to a given value.

        :param value: (float) The annual interest rate to set.

        :return: None.
        """
        self.__annualInterestRate = value

    def getMonthlyInterestRate(self):
        """
        Returns the monthly interest rate of the account.

        :return: (float) The monthly interest rate of the account.
        """
        return self.__annualInterestRate / 12

    def getMonthlyInterest(self):
        """
        Returns the monthly interest of the account.

        :return: (float) The monthly interest of the account.
        """
        return self.getMonthlyInterestRate() * self.getBalance()

    def withdraw(self, amount):
        """
        Withdraws the specified amount of money from the account.

        :param amount: (float) The amount to be withdrawn from the account.

        :return: (str) 'Success' if the withdrawal was successful, else returns 'failed'
        """
        if amount > self.__balance:
            return "failed"
        self.__balance -= amount
        return "success"

    def deposit(self, amount):
        """
        Deposits the specified amount of money to the account.

        :param amount: (float) The amount to be deposited to the account.

        :return: None.
        """
        self.__balance += amount

    def __str__(self):
        return (f"ID: {self.getID()}\nAccount Balance: $ {self.__balance}\nMonthly Interest Rate: "
                f"{self.getMonthlyInterestRate()}\nMonthly Interest: $ {self.getMonthlyInterest()}")


def main():
    # Creates an Account Object.
    account = Account(1122, 20000, 0.045)

    # Displays the current balance.
    print(f"\nAccount balance: $ {account.getBalance()}")

    # Withdraws $ 2,500 from the account.
    status = account.withdraw(2500)

    # Displays error message and terminates the program if withdraw fails or display 'success' message.
    if status == "success":
        print(f"\n$2,500 withdrawn successfully, current balance: $ {account.getBalance()}")
    elif status == "failed":
        print("\nInsufficient Funds.")
        exit(1)

    # Displays the current balance.
    print(f"\nAccount balance: $ {account.getBalance()}")

    # Deposits $3,000 into the Account.
    account.deposit(3000)

    # Display the new balance after depositing $ 3,000
    print(f"\n$3,000 deposited successfully, current balance: $ {account.getBalance()}")

    # Displays the Account Details.
    print("\n\t\tAccount Details:")
    print(f"{account.__str__()}")


if __name__ == "__main__":
    main()
