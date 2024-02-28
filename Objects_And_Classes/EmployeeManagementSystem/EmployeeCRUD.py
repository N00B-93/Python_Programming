from pickle import dump, load
from Employee import Employee


def addEmployee(fileHandler, employees):
    """
    Adds a new Employee to the EmployeeDetails file.

    :param fileHandler: (BinaryIO) The file handle to the EmployeeDetails file.

    :param employees: (dict) The EmployeeDetails dictionary.

    :return: None
    """
    try:
        employeeName = input("\nEnter your name: ")

        employeeID = int(input("\nEnter 5-digit ID number(e.g., 12345): "))

        while len(str(employeeID)) != 5:
            print("\nInvalid ID number. Use a 5-digit number.")
            employeeID = int(input("\nEnter 5-digit ID number(e.g., 12345): "))

        employeeJobTitle = input("\nEnter your Job Title: ")

        department = input("\nEnter your department: ")

        employee = Employee(employeeName, employeeID, department, employeeJobTitle)

        employees.update({employee.getEmployeeID(): employee})

        dump(employees, fileHandler)

        print(f"\n{employeeName} has been Successfully Added!")
    except Exception as exception:
        raise exception


def searchEmployee(fileHandler):
    """
    Search for an Employee in the EmployeeDetails file.

    :param fileHandler: (BinaryIO) The file handle to the EmployeeDetails file.

    :return: None
    """
    try:
        fileHandler = open("EmployeeDetails.dat", "rb")

        employeeID = int(input("\nEnter 5-digit ID number(e.g., 12345): "))

        employees: dict = load(fileHandler)

        employee = employees.get(employeeID)

        print("\nEmployee Found!")

        print(employee.__str__())
    except Exception as exception:
        raise exception


def main() -> None:
    fileHandler = open('EmployeeDetails.dat', 'wb+')
    employees = {}

    print("\n\t\t\tWelcome to Employee Management System(EMS)")

    while True:
        print("\nWhat would you like to?")
        print("""\n1. Add a new Employee.
                \n2. Search for an Employee
                \n3. Update Employee Details.
                \n4. Delete an Employee.
                \n5. Exit
                """)
        choice = input("\nEnter your choice: ")

        match choice:
            case '1':
                addEmployee(fileHandler, employees)
                choice = input("\nWould you like to continue? ('y' for yes, 'n' for no): ")
                if choice == 'y':
                    continue
                else:
                    exit(0)
            case '2':
                searchEmployee(fileHandler)
                choice = input("\nWould you like to continue? ('y' for yes, 'n' for no): ")
                if choice == 'y':
                    continue
                else:
                    exit(0)


if __name__ == '__main__':
    main()
