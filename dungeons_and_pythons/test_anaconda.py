import unittest
import anaconda


class TestAnaconda(unittest.TestCase):
    def setUp(self):
        self.a = anaconda.Anaconda(1200, 150, (2, 1.5))

    def test_anaconda_init(self):
        self.assertEqual(1200, self.a.health)
        self.assertEqual(150, self.a.damage)
        self.assertEqual((2, 1.5), self.a.berserk_tuple)
        self.assertEqual(2, self.a.attacks_till_berserk)

    def test_anaconda_to_string(self):
        self.assertEqual("big snake:\n1200/1200 health\n150 damage\n2/150% berserk",
            str(self.a))

    def test_take_damage(self):
        self.a.take_damage(100)
        self.assertEqual(1100, self.a.health)

    def test_take_damage_with_more_damage_than_health(self):
        self.a.take_damage(1300)
        self.assertEqual(0, self.a.health)

    def test_is_alive(self):
        self.assertTrue(self.a.is_alive())

    def test_is_alive_while_dead(self):
        self.a.take_damage(1200)
        self.assertFalse(self.a.is_alive())

    def test_attack(self):
        self.assertEqual(150, self.a.attack())

    def test_second_attack(self):
        self.a.attack()
        self.assertEqual(225, self.a.attack())

    def test_third_attack(self):
        self.a.attack()
        self.a.attack()
        self.assertEqual(150, self.a.attack())


if __name__ == '__main__':
    unittest.main()