from collections import defaultdict

# returns a dictionary with keys the results of 'func'
# on items from 'seq' and values - the items from 'seq'
# i.e. 'groups'['func'(item)] = item
def groupby(func, seq):
	groups = {}
	groups = defaultdict(lambda: [])

	for item in seq:
		groups[func(item)].append(item)

	return dict(groups)
 
def main():
	print(groupby(lambda x: x % 2, [0,1,2,3,4,5,6,7]))
	print(groupby(lambda x: 'odd' if x % 2 else 'even', [1, 2, 3, 5, 8, 9, 10, 12]))
	print(groupby(lambda x: x % 3, [0, 1, 2, 3, 4, 5, 6, 7]))

if __name__ == '__main__':
	main()