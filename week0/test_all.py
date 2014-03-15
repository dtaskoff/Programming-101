# my script for running all tests in
# subdirectories of '.'
import glob
from subprocess import call

def main():
    for dir_ in glob.glob("*[!.]??"):
        print("\ntests for %s"%dir_)
        call("python3.3 ./%s/tests.py"%dir_, shell = True)

if __name__ == '__main__':
    main()