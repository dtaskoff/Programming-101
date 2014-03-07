# returns list of the digits of 'n'
def number_to_list(n):	
	if n == 0:
		return []
	else:
		return number_to_list(n // 10) + [n % 10]

def main():
	print(number_to_list(123))
	print(number_to_list(99999))
	print(number_to_list(123023))


if __name__ == '__main__':
	main()