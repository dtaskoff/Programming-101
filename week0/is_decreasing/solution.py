# returns True if 'seq' is a decreasing sequence of numbers
def is_decreasing(seq):
	for index in range(1, len(seq)):
		if seq[index - 1] <= seq[index]:
			return False

	return True

def main():
	print(is_decreasing([5,4,3,2,1]))
	print(is_decreasing([1, 2, 3]))
	print(is_decreasing([100,50,20]))
	print(is_decreasing([1,1,1,1]))

if __name__ == '__main__':
	main()