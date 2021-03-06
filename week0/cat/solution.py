# a Python script that implements a part
# of the bash command 'cat'
import sys

def cat(filename):
    file_ = open(filename, "r")
    content = file_.read()
    file_.close()

    return content

def main():
    args = sys.argv
    if len(args) < 2:
        print("no filename passed")
    else:
        filename = sys.argv[1]
        print(cat(filename))

if __name__ == '__main__':
    main()