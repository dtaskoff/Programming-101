import unittest
import fight
import weapon
import entity, hero, python, anaconda


class TestFight(unittest.TestCase):
    def setUp(self):
        self.h = hero.Hero("sharik", 500, "pythonslayer")
        self.p = python.Python(100, 10)
        self.a = anaconda.Anaconda(100, 10, (2, 3))

    def test_fight_init(self):
        f = fight.Fight(self.h, self.p)
        self.assertEqual(self.h, f.hero)
        self.assertEqual(self.p, f.enemy)

    def test_simulate_with_python(self):
        f = fight.Fight(self.h, self.p)
        self.assertTrue(isinstance(f.simulate_fight(), entity.Entity))

    def test_simulate_with_anaconda(self):
        f = fight.Fight(self.h, self.a)
        self.assertTrue(isinstance(f.simulate_fight(), entity.Entity))

    def test_weapon_upgrade(self):
        w = weapon.Weapon('bow', 30, 0.50)
        self.h.equip_weapon(w)
        f = fight.Fight(self.h, self.a)
        f.simulate_fight()
        self.assertEqual(31, self.h.weapon.damage)
        self.assertEqual(0.525, self.h.weapon.critical_strike_percent)

    def test_game_over(self):
        f = fight.Fight(self.h, self.a)
        with self.assertRaises(SystemExit):
            f.game_over()

if __name__ == '__main__':
    unittest.main()