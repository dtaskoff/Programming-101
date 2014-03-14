# a script that opens the files 'filenames'
# and writes their content in MEGATRON
import sys

def concat_files(filenames):
	MEGATRON = open("MEGATRON", "a")

	for filename in filenames:
		file_ = open(filename, "r")
		MEGATRON.write(file_.read())
		MEGATRON.write("\n\n")
		file_.close()

	MEGATRON.close()

def main():
	args = sys.argv
	if len(args) < 2:
		print("no filenames passed")
	else:
		filenames = sys.argv[1:]
		concat_files(filenames)

if __name__ == '__main__':
	main()