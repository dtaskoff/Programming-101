import unittest
import github_api
import zipfile
import os
from subprocess import call

# only tests for the zipfile part are written

class TestGithubAPI(unittest.TestCase):
    def setUp(self):
        self.test_zip = zipfile.ZipFile("test.zip", "w")
        file = open("test.tst", "w")
        file.write("just a simple test\non two lines")
        file.close()
        self.test_zip.write("test.tst")

    def test_unzip_repos(self):
        self.test_zip.close()
        github_api.unzip_repos(["test"])
        self.assertTrue(os.path.exists("test.tst"))

    def test_get_extension(self):
        result = github_api.get_extension("test.tst")
        self.assertEqual(".tst", result)

    def test_print_extensions(self):
        expected = "\"*.tst\" - 1 files"
        result = github_api.print_extensions({".tst": 1})
        self.assertEqual(expected, result)

    def test_get_repos_stats(self):
        result = github_api.get_repos_stats(".")
        self.assertTrue(".tst" in result)

    def test_get_lines(self):
        self.assertEqual(2, github_api.get_lines("test.tst"))

    def tearDown(self):
        self.test_zip.close()
        call("rm -r test.tst", shell=True)
        call("rm -r test.zip", shell=True)

if __name__ == '__main__':
    unittest.main()