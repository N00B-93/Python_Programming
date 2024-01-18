from sys import exit

"""
    This is a program that prompts the user to enter the
    number of students and each student’s score, and displays the highest and secondhighest scores.

"""
# Reads in the number of students.
numberOfStudents = int(input("\nEnter the number of students: "))

# Terminates the program if the the number of students entered is < 2.
if numberOfStudents < 2:
    print("\nEnter number of student >= 2!")
    exit(0)

# Initializes the highest and second highest score variable to 0.
secondMaxScore = maxScore = 0

for i in range(0, numberOfStudents):
    # Reads in Student's score.
    score = float(input(f"\nEnter student {i + 1}'s score: "))

    if score > maxScore:
        # Assign secondMaxScore to current value of Maxcore if score > highest score.
        secondMaxScore = maxScore
        # Assign score to highest score if score > highest score.
        maxScore = score
        # Assigns a score to secondMaxScore if it's > secondMaxScore and < maxScore
    elif secondMaxScore < score < maxScore:
        secondMaxScore = score

# Displays the result.
print(f"\nHighest Score: {maxScore}\nSecond Highest Score: {secondMaxScore}")
