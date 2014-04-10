import sys
import unittest
from hashlib import sha1

sys.path.append("..")

import sql_manager


class SqlManagerTests(unittest.TestCase):

    def setUp(self):
        sql_manager.create_clients_table()
        sql_manager.register('Tester', '12aaAA**')

    def tearDown(self):
        sql_manager.cursor.execute('DROP TABLE clients')

    def test_weak_password(self):
        result = sql_manager._weak_password('tester', 'abcdefghi')
        self.assertTrue(result)

        result = sql_manager._weak_password('tester', '123456789')
        self.assertTrue(result)

        result = sql_manager._weak_password('tester', 'ABCDEFGHI')
        self.assertTrue(result)

        result = sql_manager._weak_password('tester', '*********')
        self.assertTrue(result)

        result = sql_manager._weak_password('tester', 'aaAA12**')
        self.assertFalse(result)

    def test_register(self):
        sql_manager.register('Dinko', 'abAB12*&')

        sql_manager.cursor.execute('''select Count(*)
                from clients
                where username = (?) and password = (?)''',
            ('Dinko', sha1('abAB12*&'.encode('utf-8')).digest()))
        users_count = sql_manager.cursor.fetchone()

        self.assertEqual(users_count[0], 1)

    def test_login(self):
        logged_user = sql_manager.login('Tester', '12aaAA**')
        self.assertEqual(logged_user.get_username(), 'Tester')

    def test_login_name_sql_injection(self):
        logged_user = sql_manager.login('\' OR 1=1 --', 'abc')
        self.assertFalse(logged_user)

    def test_login_wrong_password(self):
        logged_user = sql_manager.login('Tester', '123567')
        self.assertFalse(logged_user)

    def test_change_message(self):
        logged_user = sql_manager.login('Tester', '12aaAA**')
        new_message = "podaivinototam"
        sql_manager.change_message(new_message, logged_user)
        self.assertEqual(logged_user.get_message(), new_message)

    def test_change_password(self):
        logged_user = sql_manager.login('Tester', '12aaAA**')
        new_password = "12345aa**A"
        sql_manager.change_pass(new_password, logged_user)

        logged_user_new_password = sql_manager.login('Tester',
                new_password)
        self.assertEqual(logged_user_new_password.get_username(),
                'Tester')

if __name__ == '__main__':
    unittest.main()
