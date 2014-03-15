import unittest
import solution


class PrimeNumberOfDivisorsTest(unittest.TestCase):
    def test_number_of_divisors(self):
        self.assertEqual(2, solution.number_of_divisors(2))
        self.assertEqual(2, solution.number_of_divisors(101))
        self.assertEqual(9, solution.number_of_divisors(100))

    def test_prime_number_of_divisors(self):
        self.assertTrue(solution.prime_number_of_divisors(7))
        self.assertFalse(solution.prime_number_of_divisors(8))
        self.assertTrue(solution.prime_number_of_divisors(9))

if __name__ == '__main__':
    unittest.main()