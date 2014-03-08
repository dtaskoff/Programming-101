# returns the reduced version of 'path'
# according to these rules:
# .. means one directory back, . means current directory,
# every extra "/" is unnecessary and remove the last "/" (if not only one)
def reduce_file_path(path):
	path = path.split('/')
	final_path = []

	for part in path:
		if part == '..':
			if final_path:
				final_path.pop() 
		elif part != '.' and part != '/':
			final_path.append(part)

	return '/' + '/'.join(filter(lambda x: x != '', final_path))

def main():
	print(reduce_file_path("/"))
	print(reduce_file_path("/srv/../"))
	print(reduce_file_path("/srv/www/htdocs/wtf/"))
	print(reduce_file_path("/srv/www/htdocs/wtf"))
	print(reduce_file_path("/srv/./././././"))
	print(reduce_file_path("/etc//wtf/"))
	print(reduce_file_path("/etc/../etc/../etc/../"))
	print(reduce_file_path("//////////////"))
	print(reduce_file_path("/../"))
	print(reduce_file_path("/../.."))

if __name__ == '__main__':
	main()