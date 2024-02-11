"""
    A school has 100 lockers and 100 students. All lockers
    are closed on the first day of school. As the students enter, the first student,
    denoted S1, opens every locker. Then the second student, S2, begins with the
    second locker, denoted L2, and closes every other locker. Student S3 begins
    with the third locker and changes every third locker (closes it if it was open,
    and opens it if it was closed). Student S4 begins with locker L4 and changes
    every fourth locker. Student S5 starts with L5 and changes every fifth locker,
    and so on, until student S100 changes L100.
    This is a program to determine the number of lockers open after all the
    students has passed through the building and changed the lockers.
"""


def changeLocker(studentNumber, lockers):
    """
    Open or closes lockers in the locker list based on the student number.

    :param studentNumber: (int) The student number.

    :param lockers: (list) List of boolean values representing the state(open or close) of the lockers.

    :return: None.
    """
    i = 0
    if studentNumber == 1:
        while i < len(lockers):
            lockers[i] = not lockers[i]
            i += 1
    elif studentNumber == 2:
        i = 2
        while i < len(lockers):
            lockers[i] = not lockers[i]
            i += 2
    else:
        i = studentNumber
        while i < len(lockers):
            lockers[i] = not lockers[i]
            i += studentNumber


def main():
    # Creates an array of 101 boolean values.
    lockers = 101 * [False]

    # Changes the lockers from student 1 to student 100.
    for i in range(1, len(lockers)):
        changeLocker(i, lockers)

    # Displays the number of the lockers that are open after all students has passed through the locker room.
    print("\nThe lockers open after all students has passed is: ", end="")
    for i in range(1, len(lockers)):
        if lockers[i]:
            print(f"L{i} ", end="")


if __name__ == "__main__":
    main()
