# my script for testing all projects
# in all child directories, starting from '.'
import glob
from subprocess import call

def main():
    for dir_ in glob.glob("*[!.]??"):
        print("\ntests for %s"%dir_)
        call("python3.3 ./%s/tests.py"%dir_, shell = True)

if __name__ == '__main__':
    main()