# unit tests for the tic tac toe game script
import unittest
import tictactoe


class TictactoeTest(unittest.TestCase):
	def setUp(self):
		tictactoe.init()

	def test_get_board(self):
		self.assertEqual(" | | \n" * 3, tictactoe.get_board())

	def test_init(self):
		self.assertEqual(" | | \n" * 3, tictactoe.get_board())

	def test_in_board(self):
		self.assertEqual(False, tictactoe.in_board(1, 4))
		self.assertEqual(True, tictactoe.in_board(3, 2))

	def test_tic_on_empty_board(self):
		tictactoe.init()
		tictactoe.tic(1, 2)
		self.assertEqual(" |x| \n" + " | | \n" * 2, tictactoe.get_board())

	def test_tic_out_of_range(self):
		tictactoe.init()
		result = tictactoe.tic(1, 4)
		self.assertEqual(" | | \n" * 3, tictactoe.get_board())
		self.assertEqual(False, result)

	def test_tic_on_taken_field(self):
		tictactoe.init()
		tictactoe.tic(2, 3)
		result = tictactoe.tic(2, 3)
		self.assertEqual(False, result)

	def test_tic_wins_row(self):
		tictactoe.tic(2, 1)
		tictactoe.tic(2, 2)
		tictactoe.tic(2, 3)
		self.assertEqual(True, tictactoe.wins('tic'))

	def test_tic_wins_column(self):
		tictactoe.tic(1, 3)
		tictactoe.tic(2, 3)
		tictactoe.tic(3, 3)
		self.assertEqual(True, tictactoe.wins('tic'))

	def test_tic_wins_diagonal(self):
		tictactoe.tic(1, 1)
		tictactoe.tic(2, 2)
		tictactoe.tic(3, 3)
		self.assertEqual(True, tictactoe.wins('tic'))

	def test_tac_on_empty_board(self):
		tictactoe.init()
		tictactoe.tac(1, 3)
		self.assertEqual(" | |o\n" + " | | \n" * 2, tictactoe.get_board())

	def test_tac_out_of_range(self):
		tictactoe.init()
		result = tictactoe.tac(4, 1)
		self.assertEqual(" | | \n" * 3, tictactoe.get_board())
		self.assertEqual(False, result)

	def test_tac_on_taken_field(self):
		tictactoe.init()
		tictactoe.tac(2, 3)
		result = tictactoe.tac(2, 3)
		self.assertEqual(False, result)

	def test_tac_wins_row(self):
		tictactoe.tac(1, 1)
		tictactoe.tac(1, 2)
		tictactoe.tac(1, 3)
		self.assertEqual(True, tictactoe.wins('tac'))

	def test_tac_wins_column(self):
		tictactoe.tac(1, 2)
		tictactoe.tac(2, 2)
		tictactoe.tac(3, 2)
		self.assertEqual(True, tictactoe.wins('tac'))

	def test_tac_wins_diagonal(self):
		tictactoe.tac(1, 3)
		tictactoe.tac(2, 2)
		tictactoe.tac(3, 1)
		self.assertEqual(True, tictactoe.wins('tac'))

	def test_wins_with_incorrect_argument(self):
		tictactoe.tac(1, 1)
		tictactoe.tac(1, 2)
		tictactoe.tac(1, 3)
		tictactoe.tac(2, 3)
		tictactoe.tac(2, 2)
		tictactoe.tac(2, 1)
		self.assertEqual(False, tictactoe.wins('toe'))

	def test_full_board(self):
		for i in range(1, 4):
			for j in range(1, 4):
				tictactoe.tic(i, j)

		self.assertEqual(True, tictactoe.full_board())


if __name__ == '__main__':
	unittest.main()