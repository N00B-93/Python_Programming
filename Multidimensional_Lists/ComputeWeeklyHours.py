"""The weekly hours for all employees are stored in a table as shown below;

                        Su M T W Th F Sa
                Employee 0 2 4 3 4 5 8 8
                Employee 1 7 3 4 3 3 4 4
                Employee 2 3 3 4 3 3 2 2
                Employee 3 9 3 4 7 3 4 1
                Employee 4 3 5 4 3 6 3 8
                Employee 5 3 4 4 6 3 4 4
                Employee 6 3 7 4 8 3 8 4
                Employee 7 6 3 5 9 2 7 9
    This program displays employees and their total hours in decreasing order of the total hours.
"""


def main():
    # Creates arrays representing each employee's working hours.
    employee0 = [0, 2, 4, 3, 4, 5, 8, 8]
    employee1 = [1, 7, 3, 4, 3, 3, 4, 4]
    employee2 = [2, 3, 3, 4, 3, 3, 2, 2]
    employee3 = [3, 9, 3, 4, 7, 3, 4, 1]
    employee4 = [5, 3, 4, 4, 6, 3, 4, 4]
    employee5 = [5, 3, 4, 4, 6, 3, 4, 4]
    employee6 = [6, 3, 7, 4, 8, 3, 8, 4]
    employee7 = [7, 6, 3, 5, 9, 2, 7, 9]

    # An array that contains all employee working hours.
    employees = [employee0, employee1, employee2, employee3, employee4, employee5, employee6, employee7]

    # Lists to store each employee working hours and the employee index.
    totalWorkingHours = []
    employeeIndex = []

    # Calculates the total working hours for each employee.
    for row in range(len(employees)):
        totalWorkingHours.append(sum(employees[row]))
        employeeIndex.append(row)

    # Sorts the total working hours in descending order.
    for i in range(len(totalWorkingHours)):
        for j in range(1, len(employees)):
            if totalWorkingHours[j - 1] < totalWorkingHours[j]:
                totalWorkingHours[j], totalWorkingHours[j - 1] = totalWorkingHours[j - 1], totalWorkingHours[j]
                employeeIndex[j], employeeIndex[j - 1] = employeeIndex[j - 1], employeeIndex[j]

    # Displays the result.
    for i in range(len(employees)):
        print(f"\nEmployee {employeeIndex[i]} is working {totalWorkingHours[i]} hours per week.")


if __name__ == "__main__":
    main()
