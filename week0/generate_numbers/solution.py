# a script that generates 'n' numbers in some range
# and writes them in a file with the name 'filename'
import sys
from random import randint

def generate_numbers(filename, n):
    file_ = open(filename, "w")
    for i in range(0, n):
        file_.write(str(randint(1, 1000)) + " ")
    file_.close()

def main():
    args = sys.argv
    if len(args) < 3:
        print("no filename or number passed")
    else:
        filename = sys.argv[1]
        n = int(sys.argv[2])
        generate_numbers(filename, n)

if __name__ == '__main__':
    main()