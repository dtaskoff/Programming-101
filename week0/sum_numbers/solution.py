# a script that sums all numbers in a file
# with name 'filename' (containing only numbers)
import sys

def sum_numbers(filename):
    file = open(filename, "r")
    numbers = file.read().split()
    file.close()

    sum = 0
    for number in numbers:
        sum += int(number)
    return sum

def main():
    args = sys.argv
    if len(args) < 2:
        print("no filename passed")
    else:
        filename = sys.argv[1]
        print(sum_numbers(filename))

if __name__ == '__main__':
    main()