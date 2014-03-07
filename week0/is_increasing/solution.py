# returns True if 'seq' is an increasing sequence of numbers
def is_increasing(seq):
	for index in range(1, len(seq)):
		if seq[index - 1] >= seq[index]:
			return False
			
	return True

def main():
	print(is_increasing([1,2,3,4,5]))
	print(is_increasing([1]))
	print(is_increasing([5,6,-10]))
	print(is_increasing([1,1,1,1]))

if __name__ == '__main__':
	main()