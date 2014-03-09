# coordinates of the centers of our sudoku's boxes
boxes = [(1, 1), (1, 4), (1, 7),
		(4, 1), (4, 4), (4, 7),
		(7, 1), (7, 4), (7, 7)]

# coordinates of all numbers in a box if center is (0, 0)
coordinates = [(-1, -1), (-1, 0), (-1, 1),
				(0, -1), (0, 0), (0, 1),
				(1, -1), (1, 0), (1, 1)]

# generates a list which contains all numbers from
# a box with index 'i'	0 | 1 | 2
# each box contains 	3 | 4 | 5
# nine numbers			6 | 7 | 8
def box(sudoku, i):
#	takes a tuple into sudoku's coordinates
	at_index = lambda t: sudoku[t[0]][t[1]]
#	just a normal tuple addition
	add_tuples = lambda a, b: tuple(map(sum, zip(a, b)))
	index = boxes[i]

	for i in range(0, 9):
		yield at_index(add_tuples(index, coordinates[i]))

# returns True if 9x9 classic 'sudoku'
# is correctly solved
def sudoku_solved(sudoku):
	lst = []
	for i in range(0, 9):
#		here we get the rows
		lst.append(sudoku[i])
#		and the columns
		lst.append((sudoku[j][i] for j in range(0, 9)))
#		and the boxes
		lst.append(box(sudoku, i))
	row = list(range(1, 10))

	return all(map(lambda x: sorted(x) == row, lst))