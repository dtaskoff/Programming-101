import unittest
from solution import sum_numbers
from subprocess import call


class SumNumbersTest(unittest.TestCase):
    def setUp(self):
        file_ = open("test_file", "w")
        file_.write("1 2 3 4 5 6 7 8 9 10")
        file_.close()

    def test_sum_numbers(self):
        result = sum_numbers("test_file")
        self.assertEqual(55, result)

    def tearDown(self):
        call("rm -r test_file", shell = True)


if __name__ == '__main__':
    unittest.main()