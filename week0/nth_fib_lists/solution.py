# returns the n-th list in the Fibonacci sequence:
# listA is the first list
# listB is the second list
# the third list is listA + listB and so on..
def nth_fib_lists(listA, listB, n):
	while n > 1:
		listA, listB, n = listB, listA + listB, n - 1
	return listA

def main():
	print(nth_fib_lists([1], [2], 1))
	print(nth_fib_lists([1], [2], 2))
	print(nth_fib_lists([1, 2], [1, 3], 3))
	print(nth_fib_lists([], [1, 2, 3], 4))
	print(nth_fib_lists([], [], 100))

if __name__ == '__main__':
	main()