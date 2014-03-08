# a script that implements a part of
# the bash command 'wc'
import sys

def wc(command, filename):
	file = open(filename, "r")
	contents = file.read()
	file.close()

	if command == "words":
		words = contents.split()
		return len(words)
	elif command == "chars":
		return len(contents)
	elif command == "lines":
		lines = contents.splitlines()
		return len(lines)

def main():
	args = sys.argv
	if len(args) < 3:
		print("no filename or command passed")
	else:
		filename = sys.argv[1]
		command = sys.argv[2]
		print(wc(command, filename))

if __name__ == '__main__':
	main()