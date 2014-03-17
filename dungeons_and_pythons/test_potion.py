import unittest
import potion


class TestPotion(unittest.TestCase):
    def setUp(self):
        self.p = potion.Potion(100)

    def test_potion_init(self):
        self.assertEqual(100, self.p.healing_points)

    def test_potion_to_string(self):
        self.assertEqual("healing potion: 100 hp", str(self.p))


if __name__ == '__main__':
    unittest.main()