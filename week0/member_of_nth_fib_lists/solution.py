# returns True if 'needle' is member of the Fibonacci list sequence
# where the first and second list are respectively 'listA' and 'listB'
def member_of_nth_fib_lists(listA, listB, needle):
	while len(needle) > len(listA):
		listA, listB = listB, listA + listB
	return listA == needle

def main():
	print(member_of_nth_fib_lists([1, 2], [3, 4], [5, 6]))
	print(member_of_nth_fib_lists([1, 2], [3, 4], [1,2,3,4,3,4,1,2,3,4]))
	print(member_of_nth_fib_lists([7,11], [2], [7,11,2,2,7,11,2]))
	print(member_of_nth_fib_lists([7,11], [2], [11,7,2,2,7]))

if __name__ == '__main__':
	main()