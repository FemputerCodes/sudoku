import pygame
from game import game
from classes.gui.grid import Grid

pygame.font.init()

SCREEN_WIDTH = 570
SCREEN_HEIGHT = 670
GRID_WIDTH = 540
GRID_HEIGHT = 540
GRID_OFFSET = 15
GRID_ROWS = 9
GRID_COLS = 9
CELL_WIDTH = GRID_WIDTH / GRID_COLS
CELL_HEIGHT = GRID_HEIGHT / GRID_ROWS


def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Sudoku")
    screen.fill("#323232")
    clock = pygame.time.Clock()

    grid = Grid(screen, GRID_WIDTH, GRID_HEIGHT, GRID_OFFSET, GRID_ROWS, GRID_COLS)
    key = 0
    row = 0
    col = 0

    running = True

    while(running):
        grid.draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos()
                x = position[0] - GRID_OFFSET
                y = position[1] - GRID_OFFSET
                row = int(y // CELL_HEIGHT)
                col = int(x // CELL_WIDTH)
                grid.click(row, col)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_TAB:
                    key = 0
                    (row, col) = grid.next(row, col)
                    grid.click(row, col)
                if event.key == pygame.K_1 or event.key == pygame.K_KP1:
                    key = 1
                if event.key == pygame.K_2 or event.key == pygame.K_KP2:
                    key = 2
                if event.key == pygame.K_3 or event.key == pygame.K_KP3:
                    key = 3
                if event.key == pygame.K_4 or event.key == pygame.K_KP4:
                    key = 4
                if event.key == pygame.K_5 or event.key == pygame.K_KP5:
                    key = 5
                if event.key == pygame.K_6 or event.key == pygame.K_KP6:
                    key = 6
                if event.key == pygame.K_7 or event.key == pygame.K_KP7:
                    key = 7
                if event.key == pygame.K_8 or event.key == pygame.K_KP8:
                    key = 8
                if event.key == pygame.K_9 or event.key == pygame.K_KP9:
                    key = 9
                if event.key == pygame.K_DELETE or event.key == pygame.K_BACKSPACE:
                    key = 0
                grid.input(row, col, key)
        grid.check()
        if (grid.solved()):
            running = False
            
        pygame.display.flip()
        clock.tick(50)

    pygame.quit()


if __name__ == "__main__":
    # game()
    main()
