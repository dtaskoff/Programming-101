# my version of the tic tac toe game ^^

_board = [[]]
_tic_win = ['x', 'x', 'x']
_tac_win = ['o', 'o', 'o']

# initializes '_board' with the empty board
def init():
	global _board
	_board = [i.copy() for i in [[' ', ' ', ' ']] * 3]

# returns the current board's state in pretty format
def get_board():
	return '\n'.join(map('|'.join, _board)) + '\n'

# returns False, if passed position is outside the board
def in_board(row, column):
	return row >= 1 and row <= 3 and column >= 1 and column <= 3

# places tic on the given position
# (after it checks if position is correct
# if it's not, False is returned)
def tic(row, column):
	global _board

	if not in_board(row, column) or\
			_board[row - 1][column - 1] != ' ':
		return False

	_board[row - 1][column - 1] = 'x'
		
	return True

# same as for tic()
def tac(row, column):
	global _board
	
	if not in_board(row, column) or\
			_board[row - 1][column - 1] != ' ':
		return False

	_board[row - 1][column - 1] = 'o'
		
	return True

# returns True if passed argument is 'tic'
# and tic won the game, same for 'tac'
# and returns False in all other cases
def wins(tic_or_tac):
	global _board, _tic_win, _tac_win
	winner = ''

	if tic_or_tac == 'tic':
		winner = _tic_win
	elif tic_or_tac == 'tac':
		winner = _tac_win
	else:
		print("Passed incorrect argument to method wins()!")
		return False

	main_diagonal = []
	second_diagonal = []

	for i in range(0, 3):
		if _board[i] == winner or\
				[_board[j][i] for j in range(0, 3)] == winner:
			return True

		main_diagonal.append(_board[i][i])
		second_diagonal.append(_board[2 - i][i])

	return main_diagonal == winner or second_diagonal == winner

# returns True if all fields on the board are full
def full_board():
	global _board

	for i in range(0, 3):
		for j in range(0, 3):
			if _board[i][j] == ' ':
				return False

	return True

# the method that puts it all together
def main():
	instructions()
	init()
	player = 'tic'
	no_won = True

	while not full_board() and no_won:
		print('current board:\n%s'%get_board())
		position = input('%s: '%player).split()

		if len(position) != 2:
			error_message()
			continue

		position = (int(position[0]), int(position[1]))

		if player == 'tic':
			if not tic(position[0], position[1]):
				error_message()
			elif wins(player):
				print('tic beat tac')
				no_won = False
			else:
				player = 'tac'
		else:
			if not tac(position[0], position[1]):
				error_message()
			elif wins(player):
				print('tac beat tic')
				no_won = False
			else:
				player = 'tic'

	if no_won:
		print('noone won :)')

	print(get_board())

# prints some error message to the user (player(s))
def error_message():
	print('sorry, incorrect position entered..\ninput again\n')

# prints some instructions to the user (player(s))
def instructions():
	print('welcome to tic tac toe!\nenter positions in the following format:')
	print('position1 position2<enter>')
	print('press <ctrl>+<c> to exit')
	print('good luck and have fun ^^\n')

if __name__ == '__main__':
	main()