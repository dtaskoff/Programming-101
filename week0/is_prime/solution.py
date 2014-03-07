# returns True if the integer 'n' is a prime number
def is_prime(n):
	if n < 2:
		return False

	for i in range(2, n):
		if n % i == 0:
			return False

	return True
#	the short way:
#	if x < 2:
#		return False
#
#	return all(map(lambda x: n % x != 0, range(2, n)))

def main():
	print(is_prime(1))
	print(is_prime(2))
	print(is_prime(8))
	print(is_prime(11))
	print(is_prime(-10))

if __name__ == '__main__':
	main()