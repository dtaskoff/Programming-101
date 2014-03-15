import unittest
from solution import magic_string


class MagicStringTest(unittest.TestCase):
    def test_magic_string(self):
        self.assertEqual(2, magic_string(">><<><"))
        self.assertEqual(0, magic_string(">>>><<<<"))
        self.assertEqual(4, magic_string("<<>>"))
        self.assertEqual(20,
            magic_string("<><<<>>>>><<>>>>><>><<<>><><><><<><<<<<><<>>><><><"))


if __name__ == '__main__':
    unittest.main()