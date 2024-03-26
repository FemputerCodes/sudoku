import pygame
from src.styles import TEXT_COLOR, BUTTON_COLOR, BUTTON_COLOR_ACTIVE

font = pygame.font.SysFont(None, 40)

class Button():
    """Represents a clickable button in the Sudoku GUI."""

    def __init__(self, screen, grid, text, width, height, start_x, end_x, start_y, end_y):
        """Initialize the Button object.

        Args:
            screen (Surface): The pygame screen object.
            grid (Grid): The Sudoku grid object.
            text (string): The text displayed on the button.
            width (int): The width of the button.
            height (int): The height of the button.
            start_x (int): The x-coordinate of the top-left corner of the button.
            end_x (int): The x-coordinate of the bottom-right corner of the button.
            start_y (int): The y-coordinate of the top-left corner of the button.
            end_y (int): The y-coordinate of the bottom-right corner of the button.
        """
        self.screen = screen
        self.grid = grid
        self.text = text
        self.width = width
        self.height = height
        self.start_x = start_x
        self.end_x = end_x
        self.start_y = start_y
        self.end_y = end_y
        self.active = False
        self.choices = [1, 2, 3, 4, 5, 6, 7, 8, 9]


    def draw(self):
        """Draw the button on the screen."""
        solve_x = self.start_x + ((self.width - font.size(self.text)[0]) // 2)
        solve_y = self.start_y + ((self.height - font.get_height()) // 2)
        solve_font = font.render(str(self.text), True, TEXT_COLOR)
        solve_button = pygame.Rect(
            self.start_x,
            self.start_y,
            self.width,
            self.height
        )

        button_color = BUTTON_COLOR
        if self.active:
            button_color = BUTTON_COLOR_ACTIVE
        pygame.draw.rect(self.screen, button_color, solve_button, border_radius=25)
        self.screen.blit(solve_font, (solve_x, solve_y))


    def click(self):
        """Toggle the button's active state."""
        self.active = not self.active

    
    def solve(self):
        """Solve the Sudoku puzzle using the grid."""
        self.reset()
        self.grid.solve()

    
    def gui_solve(self, row, col, event):
        """Solve the Sudoku puzzle recursively using the backtracking algorithm with visual representation.

        Args:
            row (int): The current row index.
            col (int): The current column index.
            event (pygame.event): The pygame event object.

        Returns:
            bool: True if the puzzle is solved, False otherwise.
        """
        # base case 1: end of grid (success!)
        if row == len(self.grid.board.puzzle):
            return True
        # base case 2: out of bounds, go to next row
        if col == len(self.grid.board.puzzle):
            return self.gui_solve(row + 1, 0, event)
        # base case 3: not empty, go to next cell
        if self.grid.board.puzzle[row][col] != 0:
            return self.gui_solve(row, col + 1, event)
        # try possible choices
        for choice in self.choices:
            self.grid.click(row, col)
            self.grid.input(row, col, choice)
            self.grid.draw()
            pygame.display.update()
            pygame.time.delay(100)
            if self.grid.board.validate(row, col, choice):
                if self.gui_solve(row, col + 1, event):
                    return True
        # exhausted all possibilities (backtrack)
        self.grid.input(row, col, 0)
        return False
        
    def reset(self):
        """Reset the Sudoku grid."""
        for row in range(9):
            for col in range(9):
                self.grid.input(row, col, 0)
