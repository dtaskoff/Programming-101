import manage_company
import sqlite3


def create_employee():
    id_ = int(input("enter id: "))
    name = input("enter name: ")
    monthly_salary = int(input("enter monthly salary: "))
    yearly_bonus = int(input("enter yearly bonus: "))
    position = input("enter position: ")

    return {'id': id_,
            'name': name,
            'monthly_salary': monthly_salary,
            'yearly_bonus': yearly_bonus,
            'position': position}
def error():
    print("unknown command entered. try inputting <help>")

def help():
    help_ = ["list_employees", "monthly_spending", "yearly_spending",
            "add_employee", "delete_employee", "update_employee"]
    print("\n".join(help_))

def main():
    conn = sqlite3.connect("employees.db")
    cursor = conn.cursor()

    while True:
        commands = input("enter command: ")
        commands = commands.split()
        command = commands[0]

        if command == 'list_employees':
            print(manage_company.list_employees(cursor))
        elif command == 'monthly_spending':
            print(manage_company.monthly_spending(cursor))
        elif command == 'yearly_spending':
            print(manage_company.yearly_spending(cursor))
        elif command == 'add_employee':
            employee = create_employee()
            print(manage_company.add_employee(cursor, employee))
        elif command == 'exit':
            exit(0)
        elif command == 'help':
            help()
        elif len(commands) < 2:
            error()
        elif command == 'delete_employee':
            print(manage_company.delete_employee(cursor, commands[1]))
        elif command == 'update_employee':
            print(manage_company.update_employee(cursor, commands[1]))
        else:
            error()

'''
On command list_employees - Prints out all employees, in the following format - "name - position"
On command monthly_spending - Prints out the total sum for monthly spending that the company is doing for salaries
On command yearly_spending - Prints out the total sum for one year of operation (Again, salaries)
On command add_employee, the program starts to promt for data, to create a new employee.
On command delete_employee <employee_id>, the program should delete the given employee from thje database
On command update_employee <employee_id>, the program should prompt the user to change each of the fields for the given
'''

if __name__ == '__main__':
    main()