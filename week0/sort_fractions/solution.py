from functools import cmp_to_key
# returns the list 'fractions' sorted in increasing order
def sort_fractions(fractions):
	return sorted(fractions, key=cmp_to_key(\
		lambda x, y: x[0] * y[1] - x[1] * y[0]))

def main():
	print(sort_fractions([(2, 3), (1, 2)]))
	print(sort_fractions([(2, 3), (1, 2), (1, 3)]))
	print(sort_fractions([(5, 6), (22, 78), (22, 7), (7, 8), (9, 6), (15, 32)]))

if __name__ == '__main__':
	main()