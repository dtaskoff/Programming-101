import unittest
from solution import cat
from subprocess import call


class CatTest(unittest.TestCase):
    def setUp(self):
        file_ = open("test_file", "w")
        file_.write("just a simple text for testing")
        file_.close()

    def test_cat(self):
        result = cat("test_file")
        self.assertEqual("just a simple text for testing", result)

    def tearDown(self):
        call("rm -r test_file", shell = True)


if __name__ == '__main__':
    unittest.main()