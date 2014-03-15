import unittest
from solution import is_an_bn


class IsAnBnTest(unittest.TestCase):
    def test_is_an_bn(self):
        self.assertFalse(is_an_bn(""))
        self.assertFalse(is_an_bn("rado"))
        self.assertFalse(is_an_bn("aaabb"))
        self.assertTrue(is_an_bn("aaabbb"))
        self.assertFalse(is_an_bn("aabbaabb"))
        self.assertFalse(is_an_bn("bbbaaa"))
        self.assertTrue(is_an_bn("aaaaabbbbb"))
        self.assertFalse(is_an_bn("baba"))


if __name__ == '__main__':
    unittest.main()