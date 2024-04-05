class Message:
    """
    A class representing a Message.

    Attributes:
        sender (str): The sender of a message.

        recipient (str): The recipient of the message.

        messageBody (str): The content of the message.
    """
    def __init__(self, sender, recipient):
        self.sender = sender
        self.recipient = recipient
        self.messageBody = ""

    def append(self, text):
        """
        This appends a line of text to the message body.

        :param text: (str) The text to be added to the message body.

        :return: None
        """
        self.messageBody += f"\n{text}"

    def toString(self):
        """
        This returns the complete message containing the sender, recipient and the message body.

        :return: (str) The complete message containing the sender, recipient and the message body.
        """
        return f"\nFrom: {self.sender}\nTo: {self.recipient}\n{self.messageBody}"


def main():
    # Prompts the user to enter the name of the sender of the message.
    sender = input("\nEnter the sender's name: ")

    # Prompts the user to enter the name of the recipient.
    recipient = input("\nEnter the recipient's name: ")

    # Creates a message Object.
    message = Message(sender, recipient)

    while True:
        # Prompts the user to enter a message.
        text = input("\nEnter a message to be sent: ")

        # Appends a text to the message.
        message.append(text)

        # Asks if the user wants to add more message.
        option = input("\nWould you like to add more text? ('y', 'n'): ")

        # Continues with the loop if the user wants to add more messages else, breaks out of the loop.
        if option == 'y':
            continue
        else:
            break

    # Displays the message content.
    print("\n\t\tMessage Content")
    print(message.toString())


if __name__ == "__main__":
    main()
