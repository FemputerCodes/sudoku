import pygame
from pygame import Surface
from classes.cell import Cell

pygame.font.init()
font = pygame.font.SysFont(None, 40)

class Button():
    def __init__(self, cell: Cell, row: int, col: int, width: int, height):
        self.cell = cell
        self.row = row
        self.col = col
        self.width = width
        self.height = height
        self.text = ""
        self.active = False


    def draw(self, screen: Surface, offset: int):
        self.text = str(self.cell.get_number())
        if self.text == '0':
            self.text = ""
        x = offset + (self.col * self.width) + ((self.width - font.size(self.text)[0]) // 2)
        y = offset + (self.row * self.height) + ((self.height - font.get_height()) // 2)

        button_text = font.render(self.text, True, "white")
        if not self.cell.get_valid():
            button_text = font.render(self.text, True, "red")
         
        buttonframe = pygame.Rect(
                offset + self.col * self.width,
                offset + self.row * self.height,
                self.width,
                self.height,
            )
        if self.active:
            pygame.draw.rect(screen, "#555555", buttonframe)
        else:
            pygame.draw.rect(screen, "#323232", buttonframe)
        
        screen.blit(button_text, (x, y))
    

    def activate(self):
        is_fixed = self.cell.get_fixed()
        if not is_fixed:
            self.active = True

    
    def deactivate(self):
        self.active = False