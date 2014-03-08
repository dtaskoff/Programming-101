# returns string constructed in the following way:
# it has n-times "spam", where n is the highest power of 3
# such that 3^n divides 'number',
# also it has "eggs" if 5 divides 'number'
def prepare_meal(number):
	meal = []

	while number % 3 == 0:
		meal.append('spam')
		number //= 3
	if number % 5 == 0:
		if meal:
			meal.append('and')
		meal.append('eggs')

	return ' '.join(meal)
 
def main():
	print(prepare_meal(5))
	print(prepare_meal(15))
	print(prepare_meal(45))

if __name__ == '__main__':
	main()