import unittest
import solution


class SimplifyFractionTest(unittest.TestCase):
    def test_gcd(self):
        self.assertEqual(1, solution.gcd(7, 101))
        self.assertEqual(3, solution.gcd(333, 15))
        self.assertEqual(8, solution.gcd(64, 56))
    def test_simplify_fraction(self):
        self.assertEqual((1, 3), solution.simplify_fraction((3,9)))
        self.assertEqual((1, 7), solution.simplify_fraction((1,7)))
        self.assertEqual((2, 5), solution.simplify_fraction((4,10)))
        self.assertEqual((3, 22), solution.simplify_fraction((63,462)))


if __name__ == '__main__':
    unittest.main()