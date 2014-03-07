from number_to_list import number_to_list

# returns True if 'digit' is present in 'number'
def contains_digit(number, digit):
	return digit in number_to_list(number)

def main():
	print(contains_digit(123, 4))
	print(contains_digit(42, 2))
	print(contains_digit(1000, 0))
	print(contains_digit(12346789, 5))

if __name__ == '__main__':
	main()