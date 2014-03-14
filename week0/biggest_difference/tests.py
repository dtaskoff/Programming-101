import unittest
from solution import biggest_difference


class BiggestDifferenceTest(unittest.TestCase):
    def test_biggest_difference(self):
        self.assertEqual(-4, biggest_difference([1, 2, 3, 4, 5]))
        self.assertEqual(-1, biggest_difference([1,2]))
        self.assertEqual(-9, biggest_difference([-10, -9, -1]))
        self.assertEqual(-99, biggest_difference(range(100)))

    def test_biggest_difference_with_empty_list(self):
        self.assertEqual(0, biggest_difference([]))

if __name__ == '__main__':
    unittest.main()