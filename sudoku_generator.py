import math, random


class SudokuGenerator:
    '''
	create a sudoku board - initialize class variables and set up the 2D board
	This should initialize:
	self.row_length		- the length of each row
	self.removed_cells	- the total number of cells to be removed
	self.board			- a 2D list of ints to represent the board
	self.box_length		- the square root of row_length

	Parameters:
    row_length is the number of rows/columns of the board (always 9 for this project)
    removed_cells is an integer value - the number of cells to be removed

	Return:
	None
    '''

    def __init__(self, row_length, removed_cells):
        self.row_length = row_length
        self.removed = removed_cells
        self.board = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
        self.box_length = 3

    def get_board(self):
        return self.board

    def print_board(self):
        for row in self.board:
            for col in row:
                print(col, end=' ')
            print()

    def valid_in_row(self, row, num):
        if num in self.get_board()[row]:
            return False
        else:
            return True

    def valid_in_col(self, col, num):
        for x in range(9):
            if num == self.get_board()[x][col]:
                return False
        return True

    def valid_in_box(self, row_start, col_start, num):
        for r in range(row_start, row_start + 3):
            for c in range(col_start, col_start + 3):
                if self.get_board()[r][c] == num:
                    return False
        return True

    def is_valid(self, row, col, num):
        if self.valid_in_row(row, num):
            if self.valid_in_col(col, num):
                if self.valid_in_box(row//3*3, col//3*3, num):
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def fill_box(self, row_start, col_start):
        for row in range(row_start, row_start + 3):
            for col in range(col_start, col_start + 3):
                num = random.randint(1, 9)
                while not self.valid_in_box(row_start, col_start, num):
                    num = random.randint(1, 9)
                self.board[row][col] = num

    def fill_diagonal(self):
        self.fill_box(0, 0)
        self.fill_box(3, 3)
        self.fill_box(6, 6)

    def fill_remaining(self, row, col):
        if col >= self.row_length and row < self.row_length - 1:
            row += 1
            col = 0
        if row >= self.row_length and col >= self.row_length:
            return True
        if row < self.box_length:
            if col < self.box_length:
                col = self.box_length
        elif row < self.row_length - self.box_length:
            if col == int(row // self.box_length * self.box_length):
                col += self.box_length
        else:
            if col == self.row_length - self.box_length:
                row += 1
                col = 0
                if row >= self.row_length:
                    return True

        for num in range(1, self.row_length + 1):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][col] = 0
        return False

    def fill_values(self):
        self.fill_diagonal()
        self.fill_remaining(0, self.box_length)

    def remove_cells(self):
        all_coords = []
        for i in range(self.removed):
            x = random.randint(0, 8)
            y = random.randint(0, 8)
            coords = (x, y)
            while coords in all_coords:
                x = random.randint(0, 8)
                y = random.randint(0, 8)
                coords = (x, y)
            all_coords.append(coords)
            self.board[y][x] = 0

def generate_sudoku(size, removed):
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    board = sudoku.get_board()
    sudoku.remove_cells()
    board = sudoku.get_board()
    return board

