# solution to:
# http://community.topcoder.com/stat?c=problem_statement&pm=13004&rd=15842
def final_position(commands, A, B):
	position = 0
	for command in commands:
		if command == 'L' and position > -A:
			position -= 1
		elif position < B:
			position += 1

	return position