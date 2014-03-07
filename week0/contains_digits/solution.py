from number_to_list import number_to_list

# returns True if 'number' contains all 'digits'
def contains_digits(number, digits):
	list_of_digits = number_to_list(number)

	for digit in digits:
		if digit not in list_of_digits:
			return False

	return True
#	short way:
#	return all(map(lambda digit: digit in list_of_digits, digits))

def main():
	print(contains_digits(402123, [0, 3, 4]))
	print(contains_digits(666, [6,4]))
	print(contains_digits(123456789, [1,2,3,0]))
	print(contains_digits(456, []))


if __name__ == '__main__':
	main()