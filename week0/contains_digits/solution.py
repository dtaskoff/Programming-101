def number_to_list(n):  
    if n == 0:
        return []
    else:
        return number_to_list(n // 10) + [n % 10]

# returns True if 'number' contains all 'digits'
def contains_digits(number, digits):
	list_of_digits = number_to_list(number)

	for digit in digits:
		if digit not in list_of_digits:
			return False

	return True
#	short way:
#	return all(map(lambda digit: digit in list_of_digits, digits))