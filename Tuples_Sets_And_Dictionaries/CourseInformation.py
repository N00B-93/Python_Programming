"""
    This is a program that creates three dictionaries;
        1. A dictionary containing course number and room number as key-value pairs.
        2. A dictionary containing course number and instructor names as key-value pairs.
        3. A dictionary containing course number and meeting time as key-value pairs.
    Then prompts the user to enter a course number and displays the course's room number, instructor
    name and meeting time.
"""


def main() -> None:
    # Creates a dictionary containing course number and room number.
    roomNumbers = {
            'CS101': 3004,
            'CS102': 4501,
            'CS103': 6755,
            'NT110': 1244,
            'CM241': 1411
            }

    # Creates a dictionary containing course number and Instructor name.
    instructors = {
            'CS101': 'Haynes',
            'CS102': 'Alvarado',
            'CS103': 'Rich',
            'NT110': 'Burke',
            'CM241': 'Lee'
            }

    # Creates a dictionary containing course number and meeting time.
    meetingTime = {
            'CS101': '8:00 a.m',
            'CS102': '9:00 a.m',
            'CS103': '10:00 a.m',
            'NT110': '11:00 a.m',
            'CM241': '1:00 p.m'
            }

    # Displays the list of courses.
    print("\n\t\tList of Courses: ", end="")
    print("CS101 CS102 CS103 NT110 CM241")

    # Prompts the user to enter a course number.
    courseNumber = input("\nEnter your course number(e.g., CS101): ")
    try:
        # Retrieves the room number
        roomNumber = roomNumbers.get(courseNumber)
        
        # Retrieves the instructors name.
        instructor = instructors.get(courseNumber)
        
        # Retrieves the lecture time.
        time = meetingTime.get(courseNumber)
        
        # Raises a KeyError if the courseNumber entered by the user is invalid.
        if roomNumber == instructor == time is None:
            raise KeyError("Invalid course number, Use a valid course number.")
        
        # Displays the course information.
        print("\n\t\tCourse Information")
        print(f"\nCourse Number: {courseNumber}\nLecture Room Number: {roomNumber}\nCourse Instructor: "
              f"{instructor}\nLecture Time: {time}")
    except KeyError as keyError:
        print()
        print(keyError)


if __name__ == "__main__":
    main()
