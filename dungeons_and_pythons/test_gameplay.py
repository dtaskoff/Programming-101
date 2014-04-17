import unittest
import gameplay
import hero
import weapon


class TestGameplay(unittest.TestCase):
    def setUp(self):
        self.g = gameplay.Gameplay(0)

    def test_gameplay_init(self):
        self.assertEqual(0, self.g.difficulty)

    def test_pick_a_hero(self):
        hero_ = self.g.pick_a_hero("sharik")
        self.assertTrue(isinstance(hero_, hero.Hero))

    def test_add_hero(self):
        self.g.add_hero("sharik")
        self.assertTrue('dungeon' in self.g.__dict__)

    def test_vision(self):
        self.g.add_hero("sharik")
        self.assertEqual("###\n#H.\n##.", self.g.vision())

    def test_inventory_while_empty(self):
        self.g.add_hero("sharik")
        self.assertEqual("your inventory is empty", self.g.inventory())

    def test_inventory_with_weapon(self):
        self.g.add_hero("sharik")
        weapon_ = weapon.Weapon("bow", 30, 1.0)
        self.g.dungeon.hero.equip_weapon(weapon_)
        self.assertEqual("bow\n30 damage\n100% critical strike percent",
            str(self.g.inventory()))

    def test_status(self):
        self.g.add_hero("sharik")
        self.assertEqual("sharik the pythonslayer:\n400/400 health\n40 damage",
            str(self.g.status()))

    def test_instructions(self):
        self.assertEqual("available commands:\n"\
                + "move <direction = up/down/right/left>\nstatus\ninventory\nexit"\
                + "\n\nmap key:\nA - anaconda\nP - python\nH - hero\nI - item"\
                 + "\nG - gate\n\nreach the gate to go to the next level,\n"\
                + "but be careful with pythons and anacondas.\n"\
                + "they like to bite passing heroes!", self.g.instructions())

    def test_in_game(self):
        self.g.add_hero("sharik")
        self.assertTrue(self.g.in_game())
        self.g.dungeon.hero.take_damage(1000)
        self.assertFalse(self.g.in_game())

    def test_move(self):
        self.g.add_hero("sharik")
        self.assertTrue(self.g.move('right'))

    # will fail sometimes, becuse of dictionary's random iterations
    def test_list_heroes(self):
        result = self.g.list_heroes()
        expected = ["\nheroes:", "-" * 40,
                str(gameplay._heroes_by_name["sharik"]),
                "-" * 40, "-" * 40,
                str(gameplay._heroes_by_name["arya"]),
                "-" * 40, "-" * 40,
                str(gameplay._heroes_by_name["silmarillion"]), "-" * 40]
        self.assertEqual('\n'.join(expected), result)



if __name__ == '__main__':
    unittest.main()