import unittest
from solution import is_prime


class IsPrimeTest(unittest.TestCase):
    def test_is_prime(self):
        self.assertFalse(is_prime(1))
        self.assertTrue(is_prime(2))
        self.assertFalse(is_prime(8))
        self.assertTrue(is_prime(101))
        self.assertFalse(is_prime(-101))


if __name__ == '__main__':
    unittest.main()