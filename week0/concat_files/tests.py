import unittest
from solution import concat_files
from subprocess import call


class ConcatFilesTest(unittest.TestCase):
    def setUp(self):
        file_ = open("test_file1", "w")
        file_.write("just a simple text for testing")
        file_.close()

        file_ = open("test_file2", "w")
        file_.write("again just a simple text for testing")
        file_.close()

    def test_concat_files(self):
        concat_files(["test_file1", "test_file2"])
        file_ = open("MEGATRON", "r")
        content = file_.read()
        file_.close()
        self.assertEqual("just a simple text for testing\n\n"
            + "again just a simple text for testing\n\n", content)

    def tearDown(self):
        call("rm -r MEGATRON test_file?", shell = True)

if __name__ == '__main__':
    unittest.main()