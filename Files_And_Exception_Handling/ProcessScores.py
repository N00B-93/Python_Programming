"""
    This program prompts the user to enter the name of a file containing an unspecified number of scores
    then determines the total and the average of the scores.
"""


def getTotalAndAverage(listOfScores):
    """
    Returns the total and average of a list of scores.

    :param listOfScores: (list) The list of scores to ve processed.

    :return: (float), (float) The total and average score.
    """
    return sum(listOfScores), sum(listOfScores) / len(listOfScores)


def main() -> None:
    # Reads in the bame of the file containing scores.
    fileName = input("\nEnter the name of the file containing scores: ")

    try:
        fileHandler = None

        with open(fileName, 'r') as fileHandler:
            # Reads all the scores from the file as a String.
            scores = fileHandler.read()

        # Replace the occurrence of a newline character in the scores String with an empty String.
        scores = scores.replace('\n', ' ')
    
        # Creates a list of scores as Strings.
        listOfScores = scores.split()
    
        # Convert each score in the list of scores to an integer.
        listOfScores = [eval(listOfScores[i]) for i in range(len(listOfScores))]
    
        # Determine the total and average of the scores.
        total, average = getTotalAndAverage(listOfScores)

        # Displays the result.
        print(f"\nTotal: {total:.2f}\nAverage: {average:.2f}")
    except Exception as exception:
        print(exception)


if __name__ == "__main__":
    main()

