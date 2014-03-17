import unittest
import python


class TestPython(unittest.TestCase):
    def setUp(self):
        self.p = python.Python(800, 100)

    def test_python_init(self):
        self.assertEqual(800, self.p.health)
        self.assertEqual(100, self.p.damage)

    def test_python_to_string(self):
        self.assertEqual("snake:\n800/800 health\n100 damage",
            str(self.p))

    def test_take_damage(self):
        self.p.take_damage(100)
        self.assertEqual(700, self.p.health)

    def test_take_damage_with_more_damage_than_health(self):
        self.p.take_damage(900)
        self.assertEqual(0, self.p.health)

    def test_is_alive(self):
        self.assertTrue(self.p.is_alive())

    def test_is_alive_while_dead(self):
        self.p.take_damage(900)
        self.assertFalse(self.p.is_alive())

if __name__ == '__main__':
    unittest.main()