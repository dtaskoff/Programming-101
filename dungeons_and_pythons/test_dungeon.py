import unittest
import dungeon
import hero
import weapon, potion


class TestDungeon(unittest.TestCase):
    def setUp(self):
        self.d = dungeon.Dungeon(0, hero.Hero("sharik", 1000, "pythonslayer"), 0)

    def test_dungeon_init(self):
        self.assertEqual("S.P\n#.A\nI.G", self.d.map_.map_state())
        self.assertEqual(0, self.d.level)

    def test_dungeon_spawn(self):
        self.d.spawn()
        self.assertEqual("H.P\n#.A\nI.G", self.d.map_.map_state())

    def test_show_map(self):
        self.d.spawn()
        self.assertEqual("###\n#H.\n##.", self.d.show_map())
        self.d.move('right')
        self.d.move('down')
        self.assertEqual("..P\n#HA\nI.G", self.d.show_map())

    def test_get_new_position(self):
        self.d.spawn()
        self.assertEqual((1, 0), self.d._get_new_position('down'))

    def test_move(self):
        self.d.spawn()
        result = self.d.move('right')
        self.assertTrue(result)
        self.assertEqual(".HP\n#.A\nI.G", self.d.map_.map_state())

    def test_move_out_of_map_left(self):
        self.d.spawn()
        result = self.d.move('left')
        self.assertFalse(result)
        self.assertEqual("H.P\n#.A\nI.G", self.d.map_.map_state())

    def test_move_out_of_map_up(self):
        self.d.spawn()
        result = self.d.move('up')
        self.assertFalse(result)
        self.assertEqual("H.P\n#.A\nI.G", self.d.map_.map_state())

    def test_move_on_obstacle(self):
        self.d.spawn()
        result = self.d.move('down')
        self.assertFalse(result)
        self.assertEqual("H.P\n#.A\nI.G", self.d.map_.map_state())

    def test_invalid_move(self):
        self.d.spawn()
        self.d.move('own')
        self.assertEqual("H.P\n#.A\nI.G", self.d.map_.map_state())

    def test_get_item(self):
        self.d.spawn()
        self.d.move('right')
        self.d.move('down')
        self.d.move('down')
        self.d.move('left')
        self.assertEqual("..P\n#.A\nH.G", self.d.map_.map_state())

    def test_fight_with_python(self):
        self.d.spawn()
        self.d.move('right')
        self.d.move('right')
        self.assertEqual("..H\n#.A\nI.G", self.d.map_.map_state())

    def test_fight_with_anaconda(self):
        self.d.spawn()
        self.d.move('right')
        self.d.move('down')
        self.d.move('right')
        self.assertEqual("..P\n#.H\nI.G", self.d.map_.map_state())

    def test_level_up(self):
        self.d.spawn()
        self.d.move('right')
        self.d.move('down')
        self.d.move('down')
        self.assertFalse(self.d.level_up())

    def test_get_weapon(self):
        result = self.d.get_weapon()
        self.assertTrue(isinstance(result, weapon.Weapon))

    def test_get_potion(self):
        result = self.d.get_potion()
        self.assertTrue(isinstance(result, potion.Potion))

    def test_next_level(self):
        self.d.spawn()
        self.d.move('right')
        self.d.move('down')
        self.d.move('down')
        with self.assertRaises(SystemExit):
            self.d.move('right')

if __name__ == '__main__':
    unittest.main()