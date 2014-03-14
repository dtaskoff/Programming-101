import unittest
from solution import count_numbers


class CountNumbersTest(unittest.TestCase):
    def test_count_numbers(self):
        self.assertEqual(3, count_numbers([9, 2]))
        self.assertEqual(3, count_numbers([8, 2]))
        self.assertEqual(1, count_numbers([50]))
        self.assertEqual(11, count_numbers([1, 5, 8, 30, 15, 4]))
        self.assertEqual(7, count_numbers([1, 2, 4, 8, 16, 32, 64]))
        self.assertEqual(7, count_numbers([6, 2, 18]))


if __name__ == '__main__':
    unittest.main()