import pygame
from game import game
from classes.board import Board
from classes.gui.grid import Grid

pygame.font.init()

SCREEN_WIDTH = 570
SCREEN_HEIGHT = 670
GRID_WIDTH = 540
GRID_HEIGHT = 540
GRID_OFFSET = 15
GRID_ROWS = 9
GRID_COLS = 9


def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Sudoku")
    screen.fill("#323232")
    clock = pygame.time.Clock()

    board = Board() 
    grid = Grid(board, screen, GRID_WIDTH, GRID_HEIGHT, GRID_OFFSET, GRID_ROWS, GRID_COLS)

    running = True

    while(running):
        grid.draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos()
                x = position[0]
                y = position[1]
                grid.click(position)
            
        pygame.display.flip()
        clock.tick(50)

    pygame.quit()


if __name__ == "__main__":
    # game()
    main()
