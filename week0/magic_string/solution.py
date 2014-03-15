# solution to:
# http://community.topcoder.com/stat?c=problem_statement&pm=13004&rd=15842
def magic_string(string):
    count = 0
    middle = len(string) // 2
    for char in string[:middle]:
        if char == '<':
            count += 1
    for char in string[middle:]:
        if char == '>':
            count += 1
    return count