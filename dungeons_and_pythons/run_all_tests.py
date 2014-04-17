import glob
import subprocess


def main():
    tests = glob.glob("test_*.py")
    for test in tests:
        print("\nTests for %s" % test[5:])
        subprocess.call("python3.4 %s" % test, shell=True)


if __name__ == '__main__':
    main()