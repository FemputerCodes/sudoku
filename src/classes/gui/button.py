import pygame
from pygame import Surface

class Button():
    def __init__(self, row: int, col: int, width: int, height):
        self.row = row
        self.col = col
        self.width = width
        self.height = height
        self.number = 0
        self.active = False

    
    def draw(self, screen: Surface, offset: int):
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


    def activate(self):
        self.active = True

    
    def deactivate(self):
        self.active = False