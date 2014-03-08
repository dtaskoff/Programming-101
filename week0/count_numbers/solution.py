# solution to:
# http://community.topcoder.com/stat?c=problem_statement&pm=12911&rd=15843
def count_numbers(numbers):
	for number in numbers:
		possible = [number // x for x in numbers if x < number]
		possible += [x // number for x in numbers if x > number]
		list(map(lambda x: numbers.append(x) if x not in numbers else None, possible))
		
	return len(numbers)