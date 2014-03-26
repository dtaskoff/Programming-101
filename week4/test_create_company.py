import unittest
import create_company
import sqlite3
from subprocess import call


class TestCreateCompany(unittest.TestCase):
    def setUp(self):
        self.conn = sqlite3.connect("test_database.db")
        self.cursor = self.conn.cursor()

    def test_create_table(self):
        create_company.create_table(self.cursor)
        result = self.cursor.execute("SELECT * FROM employees").fetchall()
        self.assertEqual(0, len(result))

    def test_create_employee(self):
        employee = create_company.create_employee(0, "daniel taskoff", 0, 0, "tester")
        self.assertEqual({
            "id": 0,
            "name": "daniel taskoff",
            "monthly_salary": 0,
            "yearly_bonus": 0,
            "position": "tester"}, employee)

    def test_insert(self):
        create_company.create_table(self.cursor)
        employee = create_company.create_employee(0, "daniel taskoff", 0, 0, "tester")
        create_company.insert(employee, self.cursor)
        result = self.cursor.execute("SELECT * FROM employees").fetchall()
        self.assertEqual([(0, "daniel taskoff", 0, 0, "tester")], result)

    def tearDown(self):
        self.conn.close()
        call("rm -r test_database.db", shell=True)


if __name__ == '__main__':
    unittest.main()