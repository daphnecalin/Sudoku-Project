import math,random

class SudokuGenerator:
# this sets the paramters of the board, like length, of board, cells, etc.
	def __init__(self, row_length=9, removed_cells=40):
		self.row_length = row_length
		self.removed_cells = removed_cells
		self.board = [[0] * self.row_length for _ in range(self.row_length)]
		self.fill_values()
		self.remove_cells()
		
# this functiuons gets you the board based on set paramters
	
	def get_board(self):
		return self.board

# this prints the board
	def print_board(self):
		for row in self.board:
			print(row)
			
# this makes sure that a number is or is not in the baord
	def valid_in_row(self, row, num):
		return num not in self.board[row]

# this does the same as the last excpet it checks columns
	def valid_in_col(self, col, num):
		return num not in [row[col] for row in self.board]
		
# this checks if valid within the box like the row and column
	def valid_in_box(self, row_start, col_start, num):
		for i in range(3):
			for j in range(3):
				if self.board[row_start + i][col_start + j] == num:
					return False
			return True
  # if it checks out and it valid the below function executes  
   
	def is_valid(self, row, col, num):
		if num in self.board[row]:  # Checking row validity
			return False
		for i in range(self.row_length):  # Checking column validity
			if self.board[i][col] == num:
				return False
		start_row, start_col = 3 * (row // 3), 3 * (col // 3)  # Checking box validity
		for i in range(start_row, start_row + 3):
			for j in range(start_col, start_col + 3):
				if self.board[i][j] == num:
					return False
		)
		

   # this function fills in the box based on number and col and row
	def fill_box(self, row_start, col_start):
		nums = random.sample(range(1, 10), 9)
		for i in range(3):
			for j in range(3):
				self.board[row_start + i][col_start + j] = nums.pop()
	
   # this fills it in diagonally
	def fill_diagonal(self):
	 for i in range(0, self.row_length, 3):
			self.fill_box(i, i)

	
   
# this fills whatever remianing cells there are
	
	def fill_remaining(self, row, col):
		if row == self.row_length - 1 and col == self.row_length:
				return True
		if col == self.row_length:
			row += 1
			col = 0

		if self.board[row][col] != 0:
			return self.fill_remaining(row, col + 1)

		for num in range(1, self.row_length + 1):
			if self.is_valid(row, col, num):
				self.board[row][col] = num
				if self.fill_remaining(row, col + 1):
					return True
				self.board[row][col] = 0

		return False
  # this executes previous functions to fill in said values      
	def fill_values(self):
		self.fill_diagonal()
		self.fill_remaining(0, 3)

   # this function removes cells
	def remove_cells(self):
		for _ in range(self.removed_cells):
				row = random.randint(0, self.row_length - 1)
				col = random.randint(0, self.row_length - 1)
				while self.board[row][col] == 0:
					row = random.randint(0, self.row_length - 1)
					col = random.randint(0, self.row_length - 1)
				self.board[row][col] = 0
	# this generates the game and board
 
def generate_sudoku(size, removed):
	sudoku_generator = SudokuGenerator(row_length=size, removed_cells=removed)
	return sudoku_generator.get_board()
