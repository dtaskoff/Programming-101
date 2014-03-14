import unittest
from solution import cat2
from subprocess import call


class Cat2Test(unittest.TestCase):
    def setUp(self):
        file_ = open("test_file1", "w")
        file_.write("just a simple text for testing")
        file_.close()

        file_ = open("test_file2", "w")
        file_.write("again just a simple text for testing")
        file_.close()

    def test_cat2(self):
        result = cat2(["test_file1", "test_file2"])
        self.assertEqual("just a simple text for testing"
            + "\n\nagain just a simple text for testing", result)

    def tearDown(self):
        call("rm -r test_file?", shell = True)
        

if __name__ == '__main__':
    unittest.main()