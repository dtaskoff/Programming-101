# return the sum of the min and max elements in 'arr'
# ('arr' is an array that has at least one element)
def sum_of_min_and_max(arr):
	min = arr[0]
	max = arr[0]

	for element in arr:
		if min > element:
			min = element
		if max < element:
			max = element
			
	return min + max

def main():
	print(sum_of_min_and_max([1,2,3,4,5,6,8,9]))
	print(sum_of_min_and_max([-10,5,10,100]))
	print(sum_of_min_and_max([1]))

if __name__ == '__main__':
	main()