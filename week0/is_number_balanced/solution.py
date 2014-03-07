from number_to_list import number_to_list

# returns True if 'n' is balanced (i. e. has equal
# sums of digits from left and right parts:
# 1379209, 'cause 1 + 3 + 7 = 2 + 0 + 9)
def is_number_balanced(n):
	number = number_to_list(n)
	middle = len(number) // 2
	if len(number) % 2 == 0:
		return sum(number[:middle]) == sum(number[middle:])
	else:
		return sum(number[:middle]) == sum(number[middle + 1:])

def main():
	print(is_number_balanced(9))
	print(is_number_balanced(11))
	print(is_number_balanced(13))
	print(is_number_balanced(121))
	print(is_number_balanced(4518))
	print(is_number_balanced(28471))
	print(is_number_balanced(1238033))


if __name__ == '__main__':
	main()