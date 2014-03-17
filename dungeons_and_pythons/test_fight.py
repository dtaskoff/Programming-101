import unittest
import fight
import hero, python, anaconda


class TestFight(unittest.TestCase):
    def setUp(self):
        self.h = hero.Hero("sharik", 500, "pythonslayer")
        self.p = python.Python(800, 100)
        self.f = fight.Fight(self.h, self.p)

    def test_fight_init(self):
        self.assertEqual(self.h, self.f.hero)
        self.assertEqual(self.p, self.f.enemy)


if __name__ == '__main__':
    unittest.main()