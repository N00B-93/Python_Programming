"""
    This is a program that reads a list of scores and then assigns grades based on the following scheme:
        The grade is A if score is >= best – 10.
        The grade is B if score is >= best – 20.
        The grade is C if score is >= best – 30.
        The grade is D if score is >= best – 40.
        The grade is F otherwise.
"""


def getGrade(score, bestScore):
    """
    Returns a grade for a given score.

    :param score: (float) The score.

    :param bestScore: (float) The best used to determine grade.

    :return: (str) The grade.
    """
    if score >= bestScore - 10:
        return 'A'
    elif score >= bestScore - 20:
        return 'B'
    elif score >= bestScore - 30:
        return 'C'
    elif score >= bestScore - 40:
        return 'D'
    else:
        return 'F'


def main():
    # Reads in scores as a string.
    scoreString = input("\nEnter scores separated by space: ")

    # Converts the String of scores to a list of scores.
    score = scoreString.split()

    # Determines the best score.
    bestScore = eval(max(score))

    # Displays each student's score and grade.
    for i in range(len(score)):
        print(f"\nStudent {i + 1}'s score is {score[i]} and grade is {getGrade(eval(score[i]), bestScore)}")


if __name__ == '__main__':
    main()
