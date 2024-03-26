from random import randint

"""
    This is a program that sumulates a Magic 8 Ball, which is a fortune-telling toy that displays a 
random response to a yes or no question.
    The program prompts the user to ask a question and then generates a random answer to the question.
    The program continues to prompt the user to ask a question till he/she quits.
"""


def main() -> None:
    # Creates an empty list to hold responses.
    responses: list = list()

    # Opens the response.txt file, reads the responses into a list and closes the file.
    with open("response.txt") as fileHandler:
        responses = fileHandler.readlines()

    while True:
        # Prompts the user to ask a question.
        question = input("\nAsk the Oracle a question(press 0 to exit): ")

        # Breaks out of the infinite loop if user enters 0.
        if question == "0":
            break

        # Display a reponse to the user's question.
        print("\n" + responses[randint(0, 12)])


if __name__ == "__main__":
    main()

