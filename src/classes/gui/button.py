import pygame
from src.styles import TEXT_COLOR, BUTTON_COLOR, BUTTON_COLOR_ACTIVE

pygame.font.init()
font = pygame.font.SysFont(None, 40)

class Button():
    def __init__(self, screen, grid, text, width, height, start_x, end_x, start_y, end_y):
        self.screen = screen
        self.board = grid.board
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
        self.active = not self.active

    
    def gui_solve(self, row, col):
        # base case 1: end of grid (success!)
        if row == len(self.board.puzzle):
            return True
        # base case 2: out of bounds, go to next row
        if col == len(self.board.puzzle):
            return self.solve(row + 1, 0)
        # base case 3: not empty, go to next cell
        if self.board.puzzle[row][col] != 0:
            return self.solve(row, col + 1)
        # try possible choices
        for choice in self.choices:
            self.grid.input(row, col, choice)
            if self.board.validate(row, col, choice):
            #     self.update(row, col, choice)
                if self.solve(row, col + 1):
                    return True
        # exhausted all possibilities (backtrack)
        # self.update(row, col, 0)
        self.grid.input(row, col, 0)
        return False