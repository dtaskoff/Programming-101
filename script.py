from subprocess import call

# I added all of these bash-to-python methods just for the rest
# of the script to be easily read and, hopefully, understood
def ls(arguments):
	call("ls %s"%arguments, shell = True)

def rm(filename):
	call("rm -r %s"%filename, shell = True)

def mkdir(arguments):
	call("mkdir %s"%arguments, shell = True)

def mv(source, destination):
	call("mv %s %s"%(source, destination), shell = True)

def touch(name):
	call("touch %s"%name, shell = True)

def add(filename):
	call("git add %s"%filename, shell = True)

def commit(message):
	call("git commit -m \"%s\""%message, shell = True)

def push():
	call("git push origin master", shell = True)

# returns a list containing all filenames of Python scripts in current directory
def get_all_filenames():
	ls("*.py >> filenames")
	file = open("filenames", "r")
	filenames = file.read().split()
	file.close()
	rm("filenames")

	return filenames

# removes the ".py" extension from the string 'name'
def cut_extension(name):
	return name[:len(name) - 3]

# returns the same list of filenames, but without the ".py" extension
def cut_extensions(filenames):
	return list(map(cut_extension, filenames))

# makes a folder for every name in 'names'
def make_folders(names):
	for name in names:
		mkdir(name)

# moves all scripts to their corresponding folders,
# renames them to solution.py
# and adds an empty tests.py script
def move_to_folders(filenames):
	for name in filenames:
		mv("%s.py"%name, "%s/solution.py"%name)
		touch("%s/tests.py"%name)

# pretty much self-explanatory..
def push_to_repository(directories):
	for directory in directories:
		add(directory)
		commit("%s script and an empty tests file added."%directory)
		
	push()

def main():
	filenames = get_all_filenames()
	# we remove "script.py" from the list, because we don't want to
	# make anything with it
	filenames.remove("script.py")
	filenames = cut_extensions(filenames)
	make_folders(filenames)
	move_to_folders(filenames)
	push_to_repository(filenames)

if __name__ == '__main__':
	main()