"""
    This is a program that reads an unspecified number of scores and
    determines how many scores are above or equal to the average and how many
    scores are below the average. Assuming the input numbers are separated by one
    space in one line
"""


def average(scores):
    """
    Returns the average of a list of Scores.

    :param scores: (list) A list of Scores.

    :return: (float) The average of the list of Scores.
    """
    return sum(scores) / len(scores)


def main():
    # Reads in a list of numbers as a String.
    scoreString = input("\nEnter a list of scores separated by one space: ").strip()

    # Converts the string of numbers to a list of numbers.
    scores = scoreString.split()

    # Converts each element in the number list to integer or float.
    scores = list(map(eval, scores))

    # Determines the average score.
    averageScore = average(scores)

    counter1 = counter2 = counter3 = 0

    # determines the number of scores less than, equal to or greater than the average.
    for score in scores:
        if score > averageScore:
            counter1 += 1
        elif score < averageScore:
            counter2 += 1
        elif score == averageScore:
            counter3 += 1

    # Displays the result.
    print(f"\nAverage score: {averageScore:.2f}")
    print(f"\nNumber of scores above average = {counter1}\nNumber of scores below average = {counter2}\n"
          f"Number of scores equal to average = {counter3}")


if __name__ == "__main__":
    main()
