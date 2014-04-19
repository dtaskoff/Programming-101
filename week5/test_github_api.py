import unittest
import github_api
import zipfile
from subprocess import call

# only tests for the zipfile part are written

class TestGithubAPI(unittest.TestCase):
    def setUp(self):
        self.test_zip = zipfile.ZipFile("test.zip", "w")
        file = open("test", "w")
        file.write("just a simple test\non two lines")
        file.close()
        self.test_zip.write("test")

    def test_unzip_repos(self):
        github_api.unzip_repos(["test"])

    def tearDown(self):
        self.test_zip.close()
        call("rm -r test", shell=True)
        call("rm -r test.zip", shell=True)

if __name__ == '__main__':
    unittest.main()