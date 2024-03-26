import pygame
from src.classes.board import Board
from src.classes.gui.square import Square
from src.styles import GRID_COLOR, GRID_LINE_COLOR


class Grid():
    """Represents the grid containing the Sudoku board in the GUI."""

    def __init__(self, screen, width, height, width_offset, height_offset, rows, cols):
        """Initialize the Grid object.

        Args:
            screen (Surface): The pygame screen object.
            width (int): The width of the grid.
            height (int): The height of the grid.
            width_offset (int): The x-coordinate offset of the grid.
            height_offset (int): The y-coordinate offset of the grid.
            rows (int): The number of rows in the grid.
            cols (int): The number of columns in the grid.
        """

        self.screen = screen
        self.width = width
        self.height = height
        self.width_offset = width_offset
        self.height_offset = height_offset
        self.rows = rows
        self.cols = cols
        self.board = Board()
        self.squares = [
            [Square(self.board.get_cell(row, col), row, col, self.width/self.cols, self.height/self.rows) for col in range(self.cols)]
            for row in range(self.rows)
        ]


    def draw(self):
        """Draw the grid and squares on the screen."""
        gridframe = pygame.Rect(
            self.width_offset-1,
            self.height_offset-1,
            self.width+2,
            self.height+2,
        )
        pygame.draw.rect(self.screen, GRID_COLOR, gridframe, 1, border_radius=10)
        for row in range(self.rows):
            for col in range(self.cols):
                self.squares[row][col].draw(self.screen, self.width_offset, self.height_offset)
        self.__draw_horizontal_lines()
        self.__draw_vertical_lines()

    
    def __draw_horizontal_lines(self):
        """Draw horizontal grid lines."""
        cell_height = self.height / self.rows
        for i in range(1, self.rows):
            if i % 3 == 0:
                line_width = 4
            else:
                line_width = 1
            pygame.draw.line(
                self.screen,
                GRID_LINE_COLOR,
                (self.width_offset, (self.height_offset + (i * cell_height))),
                ((self.height + self.width_offset), (self.height_offset + (i * cell_height))),
                line_width,
                )


    def __draw_vertical_lines(self):
        """Draw vertical grid lines."""
        cell_width = self.width / self.cols

        for j in range(1, self.cols):
            if j % 3 == 0:
                line_width = 3
            else:
                line_width = 1
            pygame.draw.line(
                self.screen,
                GRID_LINE_COLOR,
                ((self.width_offset + (j * cell_width)), self.height_offset),
                ((self.width_offset + (j * cell_width)), (self.width + self.height_offset)),
                line_width,
                )
   
    
    def click(self, row, col):
        """Activate the selected button and deactivate any other active button.

        Args:
            row (int): The row index of the selected button.
            col (int): The column index of the selected button.
        """
        # deactivate any active buttton
        for r in range(self.rows):
            for c in range(self.cols):
                self.squares[r][c].deactivate()
        # activate selected button
        self.squares[row][col].activate()


    def next(self, row, col):
        """Get the coordinates of the next cell to be solved.

        Args:
            row (int): The current row index.
            col (int): The current column index.

        Returns:
            Tuple: The coordinates (row, col) of the next cell to solve.
        """
        return self.board.get_next(row, col+1)


    def input(self, row, col, choice):
        """Update the value of a cell in the Sudoku board.

        Args:
            row (int): The row index of the cell.
            col (int): The column index of the cell.
            choice (int): The number to be input into the cell.
        """
        self.board.update(row, col, choice)

    
    def check(self):
        """Check the validity of the Sudoku board."""
        for row in range(self.rows):
            for col in range(self.cols):
                number = self.board.puzzle[row][col]
                self.board.validate(row, col, number)
        
    
    def solved(self):
        """Check if the Sudoku puzzle is solved.

        Returns:
            bool: True if the puzzle is solved, False otherwise.
        """
        for row in range(self.rows):
            for col in range(self.cols):
                a_cell = self.board.get_cell(row, col)
                if not a_cell.get_valid():
                    return False
        return True


    def solve(self):
        """Solve the Sudoku puzzle."""
        self.board.solve(0, 0)