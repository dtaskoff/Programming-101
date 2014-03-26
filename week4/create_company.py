import sqlite3


def create_employee(id_, name, monthly_salary, yearly_bonus, position):
    return {"id": id_, "name": name, "monthly_salary": monthly_salary,
            "yearly_bonus": yearly_bonus, "position": position}

def create_table(cursor):
    cursor.execute('''CREATE TABLE employees
        (id int, name text, monthly_salary int, yearly_bonus int, position text)''')

def insert(item, cursor):
    id_ = item["id"]
    name = item["name"]
    monthly_salary = item["monthly_salary"]
    yearly_bonus = item["yearly_bonus"]
    position = item["position"]

    insert_query = "INSERT INTO employees VALUES(?, ?, ?, ?, ?)"
    cursor.execute(insert_query,
        (id_, name, monthly_salary, yearly_bonus, position))

def main():
    conn = sqlite3.connect("employees.db")
    cursor = conn.cursor()

    create_table(cursor)

    ivan = create_employee(1, "Ivan Ivanov", 5000, 10000, "Software Developer")
    rado = create_employee(2, "Rado Rado", 500, 100, "Tech Support")
    dani = create_employee(3, "Daniel Taskoff", -200, 0, "fired")

    employees = [ivan, rado, dani]

    for employee in employees:
        insert(employee, cursor)
        conn.commit()

    conn.close()


if __name__ == '__main__':
     main() 