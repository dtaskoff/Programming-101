# the standard method that returns True if 'n' is prime
def is_prime(n):
	if n < 2:
		return False

	for i in range(2, n // 2 + 1):
		if n % i == 0:
			return False

	return True

# returns all tuples which are the goldbach conjecture for 'n'
# example: 10 -> [(3, 7), (5, 5)]
def goldbach(n):
	primes = filter(lambda x: is_prime(x), range(2, n // 2 + 1))
	lst = []
	for p in primes:
		if is_prime(n - p):
			lst.append((p, n - p))
	return lst

def main():
	print(goldbach(4))
	print(goldbach(6))
	print(goldbach(8))
	print(goldbach(10))
	print(goldbach(100))

if __name__ == '__main__':
	main()