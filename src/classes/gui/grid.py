import pygame
from src.classes.board import Board
from src.classes.gui.square import Square
from src.styles import GRID_COLOR, GRID_LINE_COLOR
from pygame import Surface
from typing import Tuple


class Grid():
    def __init__(self, screen: Surface, width: int, height: int, width_offset: int, height_offset: int, rows: int, cols: int):
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
   
    
    def click(self, row: int, col: int):
        # deactivate any active buttton
        for r in range(self.rows):
            for c in range(self.cols):
                self.squares[r][c].deactivate()
        # activate selected button
        self.squares[row][col].activate()


    def next(self, row, col) -> Tuple:
        return self.board.get_next(row, col+1)


    def input(self, row: int, col: int, choice: int):
        self.board.update(row, col, choice)

    
    def check(self):
        for row in range(self.rows):
            for col in range(self.cols):
                number = self.board.puzzle[row][col]
                self.board.validate(row, col, number)
        
    
    def solved(self) -> bool:
        for row in range(self.rows):
            for col in range(self.cols):
                a_cell = self.board.get_cell(row, col)
                if not a_cell.get_valid():
                    return False
        return True

    def solve(self):
        self.board.solve(0, 0)