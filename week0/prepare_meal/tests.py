import unittest
from solution import prepare_meal


class PrepareMealTest(unittest.TestCase):
    def test_prepare_meal(self):
        self.assertEqual("eggs", prepare_meal(5))
        self.assertEqual("spam and eggs", prepare_meal(15))
        self.assertEqual("spam spam and eggs", prepare_meal(45))


if __name__ == '__main__':
    unittest.main()