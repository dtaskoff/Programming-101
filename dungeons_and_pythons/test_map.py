import unittest
import map_


class TestMap(unittest.TestCase):
    def setUp(self):
        self.m = map_.Map_("./maps/0_map")

    def test_map_init(self):
        self.assertEqual([  ['S', '.', 'P'],
                            ['#', '.', 'A'],
                            ['I', '.', 'G']], self.m.map_)
        self.assertEqual(3, self.m.height)
        self.assertEqual(3, self.m.width)

    def test_map_state(self):
        self.assertEqual("S.P\n#.A\nI.G", self.m.map_state())

    def test_spawn(self):
        result = self.m.spawn()
        self.assertEqual("H.P\n#.A\nI.G", self.m.map_state())
        self.assertTrue(result)
        result = self.m.spawn()
        self.assertFalse(result)

    def test_on_map(self):
        self.assertTrue(self.m.on_map((2, 2)))
        self.assertFalse(self.m.on_map((1, 3)))

    def test_is_obstacle(self):
        self.assertTrue(self.m.is_obstacle((1, 0)))
        self.assertFalse(self.m.is_obstacle((0, 0)))

    def test_is_gate(self):
        self.assertTrue(self.m.is_gate((2, 2)))
        self.assertFalse(self.m.is_gate((0, 0)))

    def test_is_item(self):
        self.assertTrue(self.m.is_item((2, 0)))
        self.assertFalse(self.m.is_item((0, 0)))

    def test_is_python(self):
        self.assertTrue(self.m.is_python((0, 2)))
        self.assertFalse(self.m.is_python((0, 0)))

    def test_is_anaconda(self):
        self.assertTrue(self.m.is_anaconda((1, 2)))
        self.assertFalse(self.m.is_anaconda((0, 0)))

    def test_update_map(self):
        self.m.spawn()
        self.m.update_map((0, 0), (0, 1))
        self.assertEqual(".HP\n#.A\nI.G", self.m.map_state())

    def test_visible_posistions(self):
        self.assertEqual([(-1, -1), (-1, 0), (-1, 1),
                        (0, -1), (0, 0), (0, 1),
                        (1, -1), (1, 0), (1, 1)],
            self.m._visible_positions((0, 0)))
        self.assertEqual([(0, 0), (0, 1), (0, 2),
                        (1, 0), (1, 1), (1, 2),
                        (2, 0), (2, 1), (2, 2)],
            self.m._visible_positions((1, 1)))

    def test_show_map(self):
        self.m.spawn()
        self.assertEqual("###\n#H.\n##.", self.m.show_map((0, 0)))
        self.m.update_map((0, 0), (1, 1))
        self.assertEqual("..P\n#HA\nI.G", self.m.show_map((1, 1)))


if __name__ == '__main__':
    unittest.main()