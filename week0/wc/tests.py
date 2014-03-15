import unittest
from solution import wc
from subprocess import call


class WCTest(unittest.TestCase):
    def setUp(self):
        file_ = open("test_file", "w")
        file_.write("this text has exactly:\n10 words\n48 chars\n4 lines")
        file_.close()

    def test_wc_words(self):
        self.assertEqual(10, wc('words', 'test_file'))

    def test_wc_chars(self):
        self.assertEqual(48, wc('chars', 'test_file'))

    def test_wc_lines(self):
        self.assertEqual(4, wc('lines', 'test_file'))

    def tearDown(self):
        call("rm -r test_file", shell = True)


if __name__ == '__main__':
    unittest.main()