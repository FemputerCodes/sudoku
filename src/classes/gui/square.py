import pygame
from src.styles import SQUARE_COLOR, SQUARE_COLOR_ACTIVE, TEXT_COLOR, INVALID_COLOR
from pygame import Surface
from src.classes.cell import Cell

pygame.font.init()
font = pygame.font.SysFont(None, 40)

class Square():
    def __init__(self, cell: Cell, row: int, col: int, width: int, height):
        self.cell = cell
        self.row = row
        self.col = col
        self.width = width
        self.height = height
        self.text = ""
        self.active = False


    def draw(self, screen: Surface, width_offset: int, height_offset: int):
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
        is_fixed = self.cell.get_fixed()
        if not is_fixed:
            self.active = True

    
    def deactivate(self):
        self.active = False