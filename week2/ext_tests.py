# some tests for the ext.py script
import ext
import unittest
from subprocess import call
import os

class ExtensionsTest(unittest.TestCase):

	def setUp(self):
		self.dir_name = "test_dir"
		os.mkdir(self.dir_name)
		os.chdir(self.dir_name)

	def touch(self, filename):
		call("touch %s"%filename, shell = True)

	def test_ext(self):
		self.touch("test_file.py")
		self.touch("test_file.rb")
		self.touch("test_file2.py")
		self.touch("test_file3.py")

		self.assertEqual(3, ext.ext(".", ".py"))
		self.assertEqual(1, ext.ext(".", ".rb"))
		self.assertEqual(0, ext.ext(".", "py"))

	def test_ext_with_path(self):
		os.mkdir("test_dir2")
		self.touch("test_dir2/test_file.py")
		self.assertEqual(1, ext.ext("test_dir2", ".py"))
		self.assertEqual(0, ext.ext("test_dir2", ".exe"))

	def tearDown(self):
		os.chdir("..")
		call("rm -r %s"%self.dir_name, shell = True)


if __name__ == '__main__':
    unittest.main()