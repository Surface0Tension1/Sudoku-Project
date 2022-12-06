import pygame
from sudoku_generator import *

'''
Title: Tic Tac Toe GUI
Author: Lisha Zhou
Date: Nov. 16, 2022
Code Version: Python
Availability: https://ufl.instructure.com/courses/463246/files/folder/Code/Tic%20Tac%20Toe%20GUI
'''

'''
Title: Refactor TTT_GUI in an OOP way
Author: Lisha Zhou
Date: Nov. 16, 2022
Code Version: Python
Availability: https://ufl.zoom.us/rec/play/KyPK4QSos0g-7AtLG2REAIWwC7onvQcNGL1Iy_SbZFHBp3I3YB9A3JfXpgBb-Rc5JxmGfq2ghzJAIyKn.ZgO0NPnR0UCjrXlV?autoplay=true&startTime=1668454147000
'''
pygame.init()
font = pygame.font.Font('freesansbold.ttf', 32)

# Class that represents a single cell in the Sudoku board. There are 81 Cells in a Board.
class Cell:

    # Constructor for the Cell class
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.sketch_value = 0
        self.selected = False

    # Setter for this cell’s value
    def set_cell_value(self, val):
        self.value = val

    # Setter for this cell’s sketched value
    def set_sketched_value(self, val):
        self.sketch_value = val

    # Draws this cell, along with the value inside it
    def draw(self):

        # Assigns the font type and size from pygame's pygame.font.Font function to variable cell_font

        # Assigns the red color from the constants file to variable cell_outlined_red
        cell_outlined_red = (255, 0, 0)

        # Assigns the line width to 2 (for bold outlines) to variable cell_outlined_bold
        cell_outlined_bold = 2
        x = self.col * 56
        y = self.row * 56

        # If this cell has a nonzero value, that value is displayed.
        if self.value != 0:
            text = font.render(str(self.value), True, (0, 0, 0))
            self.screen.blit(text, (x + 5, y + 5))

        elif self.sketch_value != 0:
            text = font.render(str(self.sketch_value), True, (128, 128, 128))
            self.screen.blit(text, (x+5, y+5))

        # Otherwise, no value is displayed in the cell.
        elif self.value == 0:
            text = font.render('', True, (255, 255, 255))
            self.screen.blit(text, (x + (56/2 - text.get_width()/2), y + (56/2 - text.get_height()/2)))

        #  The cell is outlined red if it is currently selected. Use (255, 0, 0) to output red
        if self.selected:
            if x >= 167:
                x -= 2
                if x >= 333:
                    x -= 2
            if y >= 167:
                y -= 2
                if y >= 333:
                    y -= 2
            pygame.draw.rect(self.screen, cell_outlined_red, (x, y, 56, 56), cell_outlined_bold)

# Class that represents an entire Sudoku board. A Board object has 81 Cell objects.
class Board:

    # Constructor for the Board class that initializes the necessary attributes to be used
    # screen is a window from Pygame, and difficulty is a variable to indicate if the user chose easy, medium, or hard.
    def __init__(self, rows, cols, width, height, screen, difficulty):
        self.rows = rows
        self.cols = cols
        self.width = width
        self.height = height
        self.model = None
        self.selected = None
        self.screen = screen
        self.difficulty = difficulty

        # Calls the initialize_board function to keep track of the 2D list
        self.og_board = generate_sudoku(self.rows, self.difficulty)
        self.board = self.og_board
        print(self.og_board)

        # Construct a list of cells by calling the Cell class and getting how many columns and rows is wanted
        self.cells = [[Cell(self.board[i][j], i, j, screen) for j in range(cols)] for i in range(rows)]

    # Draws every cell on the board and draws an outline of the Sudoku grid
    def draw(self, screen):

        # Assigns variable board_box to a 3x3 area on Sudoku board by dividing self.width by 9
        board_box = self.width / 9
        for i in range(self.rows + 1):

            # For every third cell, the line width is 2 numbers higher to have bold outlines delineate the 3x3 boxes
            if i % 3 == 0 and i != 0:
                bold_line = 3
            else:
                bold_line = 1

            # Uses LINE_COLOR from constants file as (0, 0, 0) and the bold_line variable for the line's width
            # Draws horizontal lines with screen as its surface
            # Starts at (0, i * board_box), Ends at (self.width, i * board_box)
            pygame.draw.line(
                screen,
                (0, 0, 0),
                (0, i * board_box),
                (self.width, i * board_box),
                bold_line)

            # Draws vertical lines with screen as its surface
            # Starts at (0, i * board_box, 0), ends at (i * board_box, self.height)
            pygame.draw.line(
                screen,
                (0, 0, 0),
                (i * board_box, 0),
                (i * board_box, self.height),
                bold_line)

            '''
            Title: Pygame – Drawing Objects and Shapes
            Author: Geeksforgeeks
            Date: Oct. 31, 2021
            Code Version: Python
            Availability: https://www.geeksforgeeks.org/pygame-drawing-objects-and-shapes/
            '''

        # Draws every cell on this board by looping through each row and column and using the .draw function
        for row in range(self.rows):
            for col in range(self.cols):
                self.cells[row][col].draw()

    # Marks the cell at (row, col) in the board as the current selected cell.
    # Once a cell has been selected, the user can edit its value or sketched value
    def select(self, row, col):
        # Reset all other
        row = int(row)
        col = int(col)
        for i in range(self.rows):
            for j in range(self.cols):
                self.cells[i][j].selected = False

        self.cells[row][col].selected = True
        self.selected = (row, col)
        self.cells[row][col].draw()

    # Returns a tuple of the (row, col) when a tuple of (x, y) is within the displayed board
    def click(self, x, y):
        print(x, y)

        # x and y are assigned and returned as tuple (row, col) if x is less than width and y is less than height
        if x < self.width and y < self.height + 100:
            print(f'coordinates are in range of board {self.width}, {self.height}')
            board_box = self.width / 9
            print(self.width, board_box)
            row = x // board_box
            col = y // board_box
            print(row, col)
            return col, row

        # Otherwise, the tuple of (x, y) is out of range of the displayed board, so None is returned
        else:
            print('coordinates are out of range of board')
            return None

    # Clears the value cell. Note that the user can only remove the cell values and sketched value that are
    # filled by themselves.
    def clear(self):
        row, col = self.selected
        if self.og_board[row][col] == 0:
            self.cells[row][col].set_cell_value(0)
            self.cells[row][col].set_sketched_value(0)

    # Sets the sketched value of the current selected cell equal to user entered value
    def sketch(self, val):
        row, col = self.selected
        self.cells[row][col].set_sketched_value(val)
        # It will be displayed at the top left corner of the cell using the draw() function

    # Sets the value of the current selected cell equal to user entered value; Called when user presses the Enter key
    def place_number(self, val):
        row, col = self.selected
        if self.cells[row][col].value == 0:
            self.cells[row][col].set_cell_value(val)
            self.cells[row][col].set_sketched_value(0)
            self.update_board()
            return False

    # Reset all cells in the board to their original values (0 if cleared, otherwise the corresponding digit).
    def reset_to_original(self):
        for i in range(self.rows):
            for j in range(self.cols):
                self.cells[i][j].set_sketched_value(0)
                self.cells[i][j].set_cell_value(self.og_board[i][j])
        self.update_board()

    # Returns a Boolean value indicating whether the board is full or not
    def is_full(self):

        # Iterates through 9 rows and columns to double index and check if the cell is empty or not
        for row in range(9):
            for col in range(9):

                # Returns False if a cell value equals 0, indicating that it is empty so the board is not full
                if self.board[row][col] == 0:
                    return False

        # Returns True if all cell values do not equal 0, indicating that no cells are empty and the board is full
        return True

    # Updates the underlying 2D board with the values in all cells
    def update_board(self):
        self.board = [[self.cells[i][j].value for j in range(self.cols)] for i in range(self.rows)]


    # Finds an empty cell and returns its row and col as a tuple (x, y)
    def find_empty(self):

        # Iterates through 9 rows and columns to double index and check if the cell is empty or not
        for row in range(9):
            for col in range(9):

                # row and col are returned as a tuple if the value is equal to 0, indicating that it is empty
                if self.board[row][col] == 0:
                    return row, col

        # Otherwise, None is returned since it is not empty
        return None


    # Check whether the Sudoku board is solved correctly.
    def check_board(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.cells[i][j].value in self.board[i]:
                    return False

                if self.cells[i][j].value == [self.board[x][j] for x in range(self.rows)]:
                    return False

                if self.cells[i][j].value == [[self.board[r][c] for c in range(j//3*3, j//3*3 +3)] for r in range(i//3*3, i//3*3 + 3)]:
                    return False
        return True

