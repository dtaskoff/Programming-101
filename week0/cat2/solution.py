# a Python script that implements a part
# of the bash command 'cat'
import sys

def cat(filename):
    file_ = open(filename, "r")
    content = file_.read()
    file_.close()

    return content

def cat2(filenames):
	text = map(cat, filenames)
	return "\n\n".join(text)

def main():
	args = sys.argv
	if len(args) < 2:
		print("no filenames passed")
	else:
		filenames = sys.argv[1:]
		print(cat2(filenames))

if __name__ == '__main__':
    main()