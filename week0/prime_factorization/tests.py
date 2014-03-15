import unittest
from solution import prime_factorization


class PrimeFactorizationTest(unittest.TestCase):
    def test_prime_factorization(self):
        self.assertEqual([(2, 1), (5, 1)].sort(), prime_factorization(10).sort())
        self.assertEqual([(2, 1), (7, 1)].sort(), prime_factorization(14).sort())
        self.assertEqual([(2, 2), (89, 1)].sort(), prime_factorization(356).sort())
        self.assertEqual([(89, 1)], prime_factorization(89))
        self.assertEqual([(2, 3), (5, 3)].sort(), prime_factorization(1000).sort())


if __name__ == '__main__':
    unittest.main()