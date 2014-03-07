from number_to_list import number_to_list

# returns True if 'n' is a palindrom
def is_int_palindrom(n):
	reversed = number_to_list(n)
	reversed.reverse()

	if reversed == number_to_list(n):
		return True

	return False

def main():
	print(is_int_palindrom(1))
	print(is_int_palindrom(42))
	print(is_int_palindrom(100001))
	print(is_int_palindrom(999))
	print(is_int_palindrom(123))


if __name__ == '__main__':
	main()