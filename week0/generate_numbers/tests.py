import unittest
from solution import generate_numbers
from subprocess import call


class GenerateNumbersTest(unittest.TestCase):
    def test_generate_numbers(self):
        generate_numbers("test_file", 100)
        file_ = open("test_file", "r")
        size = len(file_.read().split())
        file_.close()
        self.assertEqual(100, size)

    def tearDown(self):
        call("rm -r test_file", shell = True)


if __name__ == '__main__':
    unittest.main()