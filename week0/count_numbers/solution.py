# solution to:
# http://community.topcoder.com/stat?c=problem_statement&pm=12911&rd=15843
def count_numbers(numbers):
    for number in numbers:
        possible = [number // x for x in numbers if x < number]
        possible += [x // number for x in numbers if x > number]
        
        for x in possible:
            if x not in numbers:
                numbers.append(x)        
    return len(numbers)