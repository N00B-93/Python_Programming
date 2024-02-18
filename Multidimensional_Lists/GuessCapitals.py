"""
    This is a program that repeatedly prompts the user to enter a
    capital for a state. Upon receiving the user input, the program reports whether
    the answer is correct.
    The number of questions answered corrected is displayed at the end of the program.
"""


def main():
    # 2-D list that holds all the states in Nigeria and their capitals.
    statesAndCapitals = [['Abia', 'Umuahia'],
                         ['Adamawa', 'Yola'],
                         ['Akwa Ibom', 'Uyo'],
                         ['Anambra', 'Awka'],
                         ['Bauchi', 'Bauchi'],
                         ['Bayelsa', 'Yenagoa'],
                         ['Benue', 'Markurdi'],
                         ['Cross River', 'Calabar'],
                         ['Delta', 'Asaba'],
                         ['Ebonyi', "Abakaliki"],
                         ['Edo', 'Benin City'],
                         ['Ekiti', 'Ado Ekiti'],
                         ['Enugu', 'Enugu'],
                         ['Gombe', 'Gombe'],
                         ['Imo', 'Owerri'],
                         ['Jigawa', 'Dutse'],
                         ['Kaduna', 'Kaduna'],
                         ['Kano', 'Kano'],
                         ['Katsina', 'Katsina'],
                         ['Kebbi', 'Birin Kebbi'],
                         ['Kogi', 'Lokoja'],
                         ['Kwara', 'Ilorin'],
                         ['Lagos', 'Ikeja'],
                         ['Nassarawa', 'Lafia'],
                         ['Niger', 'Minna'],
                         ['Ogun', 'Abeokuta'],
                         ['Ondo', 'Akure'],
                         ['Osun', 'Osogbo'],
                         ['Oyo', 'Ibadan'],
                         ['Plateau', 'Jos'],
                         ['Rivers', 'Port Harcourt'],
                         ['Sokoto', 'Sokoto'],
                         ['Taraba', 'Jalingo'],
                         ['Yobe', 'Damaturu'],
                         ['Zamfara', 'Gusau'],
                         ['FCT', 'Abuja']
                         ]

    # Variable used to count the number of questions answered correctly.
    correctCount = 0

    # Prompts the user to enter the capital of each state.
    for i in range(len(statesAndCapitals)):
        answer = input(f"\nWhat is the capital of {statesAndCapitals[i][0]}? ")
        if answer.lower() == statesAndCapitals[i][1].lower():
            print("\nYour Answer is correct!")
            correctCount += 1
        else:
            print(f"\nWrong! The correct answer is: {statesAndCapitals[i][1]}")

    # Displays the number of questions answered correctly.
    print(f"\nYou got {correctCount} correct.")


if __name__ == '__main__':
    main()
