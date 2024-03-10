import pygame
from classes.board import Board
from classes.gui.button import Button
from pygame import Surface
from typing import Tuple


class Grid():
    def __init__(self, screen: Surface, width: int, height: int, offset: int, rows: int, cols: int):
        self.screen = screen
        self.width = width
        self.height = height
        self.offset = offset
        self.rows = rows
        self.cols = cols
        self.board = Board()
        self.buttons = [
            [Button(self.board.get_cell(row, col), row, col, self.width/self.cols, self.height/self.rows) for col in range(self.cols)]
            for row in range(self.rows)
        ]


    def draw(self):
        for row in range(self.rows):
            for col in range(self.cols):
                self.buttons[row][col].draw(self.screen, self.offset)
        self.__draw_horizontal_lines()
        self.__draw_vertical_lines()

    
    def __draw_horizontal_lines(self):
        cell_height = self.height / self.rows
        for i in range(0, self.rows + 1):
            if i % 3 == 0:
                line_width = 4
            else:
                line_width = 1
            pygame.draw.line(
                self.screen,
                "white",
                (self.offset, (self.offset + (i * cell_height))),
                ((self.height + self.offset), (self.offset + (i * cell_height))),
                line_width,
                )


    def __draw_vertical_lines(self):
        cell_width = self.width / self.cols

        for j in range(0, self.cols + 1):
            if j % 3 == 0:
                line_width = 4
            else:
                line_width = 1
            pygame.draw.line(
                self.screen,
                "white",
                ((self.offset + (j * cell_width)), self.offset),
                ((self.offset + (j * cell_width)), (self.width + self.offset)),
                line_width,
                )
    

    def click(self, position: Tuple) -> Tuple:
        x = position[0] - self.offset
        y = position[1] - self.offset

        cell_width = self.width / self.cols
        cell_height = self.height / self.rows

        position_row = int(y // cell_height)
        position_col = int(x // cell_width)

        # deactivate any active buttton
        for row in range(self.rows):
            for col in range(self.cols):
                self.buttons[row][col].deactivate()
        
        # activate selected button
        self.buttons[position_row][position_col].activate()
        return (position_row, position_col)


    def input(self, row: int, col: int, choice: int):
        self.board.update(row, col, choice)

    
    def check(self):
        for row in range(self.rows):
            for col in range(self.cols):
                number = self.board.puzzle[row][col]
                self.board.validate(row, col, number)
