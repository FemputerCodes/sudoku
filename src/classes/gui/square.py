import pygame
from src.styles import SQUARE_COLOR, SQUARE_COLOR_ACTIVE, TEXT_COLOR, INVALID_COLOR
from src.classes.cell import Cell

pygame.font.init()
font = pygame.font.SysFont(None, 40)

class Square():
    """Represents a square on the Sudoku grid."""

    def __init__(self, cell, row, col, width, height):
        """Initialize the Square object.

        Args:
            cell (Cell): The cell object associated with the square.
            row (int): The row index of the square.
            col (int): The column index of the square.
            width (int): The width of the square.
            height (int): The height of the square.
        """

        self.cell = cell
        self.row = row
        self.col = col
        self.width = width
        self.height = height
        self.text = ""
        self.active = False


    def draw(self, screen, width_offset, height_offset):
        """Draw the square on the screen.

        Args:
            screen (Surface): The pygame screen object.
            width_offset (int): The x-coordinate offset of the square.
            height_offset (int): The y-coordinate offset of the square.
        """
        self.text = str(self.cell.get_number())
        if self.text == '0':
            self.text = ""
        x = width_offset + (self.col * self.width) + ((self.width - font.size(self.text)[0]) // 2)
        y = height_offset + (self.row * self.height) + ((self.height - font.get_height()) // 2)

        square_text = font.render(self.text, True, TEXT_COLOR)
        if not self.cell.get_valid():
            square_text = font.render(self.text, True, INVALID_COLOR)
         
        squareframe = pygame.Rect(
                width_offset + self.col * self.width,
                height_offset + self.row * self.height,
                self.width,
                self.height,
            )
        
        square_color = SQUARE_COLOR
        if self.active:
            square_color = SQUARE_COLOR_ACTIVE
        
        if self.row == 0 and self.col == 0:
            pygame.draw.rect(screen, square_color, squareframe, border_top_left_radius=10)
        elif self.row == 0 and self.col == 8:
            pygame.draw.rect(screen, square_color, squareframe, border_top_right_radius=10)
        elif self.row == 8 and self.col == 0:
            pygame.draw.rect(screen, square_color, squareframe, border_bottom_left_radius=10)
        elif self.row == 8 and self.col == 8:
            pygame.draw.rect(screen, square_color, squareframe, border_bottom_right_radius=10)
        else:
            pygame.draw.rect(screen, square_color, squareframe)
        
        screen.blit(square_text, (x, y))
    

    def activate(self):
        """Activate the square if it's not fixed."""
        is_fixed = self.cell.get_fixed()
        if not is_fixed:
            self.active = True

    
    def deactivate(self):
        """Deactivate the square."""
        self.active = False


    def get_active_state(self):
        """Get the active state of the square.

        Returns:
            bool: True if the square is active, False otherwise.
        """
        return self.active