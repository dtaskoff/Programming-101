# returns the sum of the digits of 'n' (n is an integer)
def sum_of_digits(n):
	sum = 0
	if n < 0:
		n = (-n)
		
	while n > 0:
		sum += n % 10
		n //= 10
	return sum