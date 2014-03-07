# returns the sum of the digits of 'n' (n is an integer)
def sum_of_digits(n):
	if n < 0:
		return sum_of_digits(-n)
	if n == 0:
		return 0
		
	return n % 10 + sum_of_digits(n // 10)

def main():
	print(sum_of_digits(1325132435356))
	print(sum_of_digits(123))
	print(sum_of_digits(6))
	print(sum_of_digits(-10))

if __name__ == '__main__':
	main()