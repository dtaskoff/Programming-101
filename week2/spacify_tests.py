# tests(test) for the spacify script

import spacify
import unittest
from subprocess import call

class SpacifyTest(unittest.TestCase):
	"""Testing my spacify script"""
	def setUp(self):
		self.file_name = "test_file"
		self.file_handler = open(self.file_name, "w+")

	def test_spacify(self):
		self.file_handler.write("my\tfile for testing\tthe\nspacify\tfunction")
		self.file_handler.seek(0)
		spacify.spacify(self.file_name)

		self.file_handler.seek(0)
		function_content = self.file_handler.read()
		test_content = "my    file for testing    the\nspacify    function"
		self.assertEqual(test_content, function_content)

	def tearDown(self):
		self.file_handler.close()
		call("rm -r test_file", shell = True)

if __name__ == '__main__':
    unittest.main()