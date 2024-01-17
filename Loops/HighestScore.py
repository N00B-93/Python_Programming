"""
    This is a program that prompts the user to enter the number
of students and each student’s score, and displays the highest score.
"""
# Reads in a score.
score = int(input("\nEnter a Score: "))

# Reads in number of Students.
numberOfStudents = score

# Initializes the highest score with the first score.
maxScore = score

# Loop that continues to read score while score is not 0.
for i in range(numberOfStudents):
    score = int(input())
    if score > maxScore:
        maxScore = score  # Update the highest score if the current score is greater than it.

# Displays the highest score.
print(f"\n\nThe highest score is: {maxScore}")
