import unittest
from solution import is_number_balanced


class IsNumberBalanced(unittest.TestCase):
    def test_is_number_balanced(self):
        self.assertTrue(is_number_balanced(9))
        self.assertTrue(is_number_balanced(11))
        self.assertFalse(is_number_balanced(13))
        self.assertTrue(is_number_balanced(121))
        self.assertTrue(is_number_balanced(4518))
        self.assertFalse(is_number_balanced(28471))
        self.assertFalse(is_number_balanced(123803))


if __name__ == '__main__':
    unittest.main()