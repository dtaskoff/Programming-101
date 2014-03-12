# some tests for the string_utils module
import string_utils
import unittest

class StringUtilsTest(unittest.TestCase):
	"""Testing my string utils module"""
	def test_lines(self):
		self.assertEqual(["some", "new", "lines"], string_utils.lines("some\nnew\nlines"))
		self.assertEqual(["some", "new", "lines too"],
			string_utils.lines("some\nnew\nlines too\n"))

	def test_unlines(self):
		self.assertEqual("some\nnew\nlines", string_utils.unlines(["some", "new", "lines"]))

	def test_words(self):
		self.assertEqual(["some", "words", "here"], string_utils.words("some words here"))
		self.assertEqual(["some", "words", "here", "too"],
			string_utils.words("some\twords\nhere too"))

	def test_unwords(self):
		self.assertEqual("some words here", string_utils.unwords(["some", "words", "here"]))

	def test_tabs_to_spaces(self):
		self.assertEqual("my    test for the    example",
			string_utils.tabs_to_spaces("my\ttest for the\texample"))
		self.assertEqual("my  other test for the  example",
			string_utils.tabs_to_spaces("my\tother test for the\texample", 2))

if __name__ == '__main__':
    unittest.main()