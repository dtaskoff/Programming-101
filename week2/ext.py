# a script that takes two argumens:
# a directory and an extension, and
# prints the number of files with that
# extension in the directory
 
import os

def ext(path, extension):
	if not extension.startswith('.'):
		return 0

	count = 0

	for filename in os.listdir(path):
		if filename.endswith(extension) and os.path.isfile("%s/%s"%(path, filename)):
			count += 1
	return count

def main():
	args = sys.argv

	if len(args) < 3:
		print("directory or extension not passed!")
	else:
		ext(args[1], args[2])