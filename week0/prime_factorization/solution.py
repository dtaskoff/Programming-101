from is_prime import is_prime

# returns a list of tuples representing the prime factorization of 'n'
def prime_factorization(n):
	current = n
	primes = [p for p in range(2, n + 1) if is_prime(p) and n % p == 0]
	# factorization is a dictionary with keys - the primes
	# and values - the powers of these primes in the factorization of 'n'
	factorization = {}
	index = 0

	while index < len(primes):
		p = primes[index]

		if current % p == 0:
			current //= p
			if p in factorization:
				factorization[p] += 1
			else:
				factorization[p] = 1
		else:
			index += 1

	# just making the result to be an array of tuples
	return list(map(lambda p: (p, factorization[p]), factorization))


def main():
	print(prime_factorization(10))
	print(prime_factorization(14))
	print(prime_factorization(356))
	print(prime_factorization(89))
	print(prime_factorization(1000))


if __name__ == '__main__':
	main()