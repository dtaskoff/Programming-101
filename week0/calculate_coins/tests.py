import unittest
from solution import calculate_coins


class CalculateCoinsTest(unittest.TestCase):
    def test_calculate_coins(self):
        self.assertEqual({ 1: 1, 2: 1, 5: 0, 10: 0, 20: 0, 50: 1, 100: 0 },
            calculate_coins(0.53))
        self.assertEqual({ 1: 0, 2: 2, 5: 0, 10: 0, 20: 2, 50: 1, 100: 8 },
            calculate_coins(8.94))

if __name__ == '__main__':
    unittest.main()