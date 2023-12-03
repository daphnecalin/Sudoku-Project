import pygame
from cell import Cell

class Board:
    #initializes board attributes
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.cells = self.create_board()


    def draw(self):
        #fills screen with white
        self.screen.fill((255, 255, 255))
        #draws grid
        cell_width = self.width // 9
        cell_height = self.height // 9

        for i in range(0, self.width + 1, cell_width):
            line_thickness = 3 if i % (3 * cell_width) == 0 else 1  # Bold lines for 3x3 boxes
            pygame.draw.line(self.screen, (0, 0, 0), (i, 0), (i, self.height), line_thickness)
            pygame.draw.line(self.screen, (0, 0, 0), (0, i), (self.width, i), line_thickness)

        #draws cells
        for row in self.cells:
            for cell in row:
                cell.draw()

        #updates displat after drawing
        pygame.display.flip()

        #redrawing just in case for more clarity
        for i in range(0, self.width + 1, self.width // 9):
            pygame.draw.line(self.screen, (0, 0, 0), (i, 0), (i, self.height))
            pygame.draw.line(self.screen, (0, 0, 0), (0, i), (self.width, i))

        # Draw each cell again just in case
        for row in self.cells:
            for cell in row:
                cell.draw()


    def select(self, row, col):
        #checks for a previous selected cell, then deselct
        if self.selected_cell:
            self.selected_cell.deselect()
        #sets new selected cell
        self.selected_cell = self.cells[row][col]
        self.selected_cell.select()


    def click(self, x, y):
        #row and columns
        cell_width = self.width // 9
        cell_height = self.height // 9
        #calculates row and column indices
        row = y // cell_height
        col = x // cell_width
        #this checks if the clicks are within the area/coordinates in the Sudoku board
        if 0 <= row < 9 and 0 <= col < 9:
            return row, col
        else:
            return None #if outside then nothing happens


    def clear(self):
        #checks if the cell is selected and not filled
        if self.selected_cell and not self.selected_cell.is_initial():
            self.selected_cell.clear_value() #clears val of selected cell


    def sketch(self, value):
        #checks if there is a cell that is selected
        if self.selected_cell:
            self.selected_cell.set_sketched_value(value)


    def place_number(self, value):
        # Check if there is a selected cell
        if self.selected_cell:
            self.selected_cell.set_value(value)


    def reset_to_original(self):
        #goes through each cell in board
        for row in self.cells:
            for cell in row:
                #cheks if the cell is not already filled
                if not cell.is_initial():
                    cell.clear_value()


    def is_full(self):
        #checks through each cell
        for row in self.cells:
            #checks if empty, empty is the value of 0
            for cell in row:
                if cell.value == 0:
                    return False
        return True


    def update_board(self):
        #This updates the board with values each of the cells
        for row_idx, row in enumerate(self.cells):
            for col_idx, cell in enumerate(row):
                #updates boards cells value
                self.cells[row_idx][col_idx] = cell.value


    def find_empty(self):
        #finds the first empty cell on board, returns row and column indices
        for row_idx, row in enumerate(self.cells):
            for col_idx, cell in enumerate(row):
                #checks if cell is empty, empty is 0
                if cell.value == 0:
                    return row_idx, col_idx
        return None #returns nothing if it is not empty


    def check_board(self):
        # Check rows, columns, boxes for duplicates
        for i in range(9):
            #checks row
            if not self.is_valid(self.cells[i]):
                return False
            # Check columns
            if not self.is_valid([row[i] for row in self.cells]):
                return False
        #checks 3x3 boxes for duplicate
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                #takes out the values from box
                box_values = [
                    self.cells[row][col].value
                    for row in range(i, i + 3)
                    for col in range(j, j + 3)
                ]
                #checks through the values that were extracted for any duplicates
                if not self.is_valid(box_values):
                    return False
        #if no duplicates found in row,columns, or boxes then the board is valid
        return True



