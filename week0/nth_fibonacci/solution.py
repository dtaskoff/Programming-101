# returns the n-th number in the Fibonacci series (1, 1, 2, 3, 5..)
def nth_fibonacci(n):
	if n < 1:
		print("Oops, that wasn't a valid input..\nInput a positive number")
	elif n <= 2:
		return 1
	else:
		return nth_fibonacci(n - 1) + nth_fibonacci(n - 2)

def main():
	print(nth_fibonacci(1))
	print(nth_fibonacci(2))
	print(nth_fibonacci(3))
	print(nth_fibonacci(10))

if __name__ == '__main__':
	main()