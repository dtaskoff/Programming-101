# a script that takes a filename as argument
# and if such a file exists in current directory
# replaces all tabs in it with 4 spaces

from string_utils import tabs_to_spaces

def spacify(filename):
	f = open(filename, "r+")
	content = f.read()
	f.seek(0)

	f.write(tabs_to_spaces(content))
	f.close()

def main():
	args = sys.argv

	if len(args) < 2:
		print("filename not passed!")
	else:
		spacify(args[1])