import asyncio
import pygame
from src.game import game
from src.styles import SCREEN_COLOR
from src.classes.gui.grid import Grid
from src.classes.gui.button import Button
import time

pygame.init()
pygame.font.init()
font = pygame.font.SysFont(None, 40)

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 670
GRID_WIDTH = 540
GRID_HEIGHT = 540
GRID_WIDTH_OFFSET = (SCREEN_WIDTH - GRID_WIDTH) / 2
GRID_HEIGHT_OFFSET = 15
GRID_ROWS = 9
GRID_COLS = 9
CELL_WIDTH = GRID_WIDTH / GRID_COLS
CELL_HEIGHT = GRID_HEIGHT / GRID_ROWS

SOLVE_WIDTH = 120
SOLVE_HEIGHT = 60
SOLVE_START_X = (SCREEN_WIDTH / 2) - (SOLVE_WIDTH + 5)
SOLVE_END_X = SOLVE_START_X + SOLVE_WIDTH
SOLVE_START_Y = GRID_HEIGHT + (2 * GRID_HEIGHT_OFFSET)
SOLVE_END_Y = SOLVE_START_Y + SOLVE_HEIGHT

RESET_WIDTH = 120
RESET_HEIGHT = 60
RESET_START_X = (SCREEN_WIDTH / 2) + 5
RESET_END_X = RESET_START_X + RESET_WIDTH
RESET_START_Y = GRID_HEIGHT + (2 * GRID_HEIGHT_OFFSET)
RESET_END_Y = RESET_START_Y + RESET_HEIGHT


def redraw(screen, grid, solver, reset, play_time):
    screen.fill(SCREEN_COLOR)
    # draw time
    # text = font.render("Time: " + str(play_time) + " seconds", 1, (0,0,0))
    # screen.blit(text, (SCREEN_WIDTH-250, SCREEN_HEIGHT-40))
    # draw grid and buttons
    grid.draw()
    solver.draw()
    reset.draw()

async def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.fill(SCREEN_COLOR)
    pygame.display.set_caption("Sudoku")
    
    clock = pygame.time.Clock()

    grid = Grid(screen, GRID_WIDTH, GRID_HEIGHT, GRID_WIDTH_OFFSET, GRID_HEIGHT_OFFSET, GRID_ROWS, GRID_COLS)
    solver = Button(screen, grid, "SOLVE", SOLVE_WIDTH, SOLVE_HEIGHT, SOLVE_START_X, SOLVE_END_X, SOLVE_START_Y, SOLVE_END_Y)
    reset = Button(screen, grid, "RESET", RESET_WIDTH, RESET_HEIGHT, RESET_START_X, RESET_END_X, RESET_START_Y, RESET_END_Y)

    key = 0
    row = 0
    col = 0

    running = True
    start = time.time()

    while(running):
        play_time = round(time.time() - start)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos()
                if GRID_WIDTH_OFFSET <= position[0] <= (GRID_WIDTH + GRID_WIDTH_OFFSET) and GRID_HEIGHT_OFFSET <= position[1] <=(GRID_HEIGHT + GRID_HEIGHT_OFFSET):
                    x = position[0] - GRID_WIDTH_OFFSET
                    y = position[1] - GRID_HEIGHT_OFFSET
                    row = int(y // CELL_HEIGHT)
                    col = int(x // CELL_WIDTH)
                    grid.click(row, col)
                elif SOLVE_START_X <= position[0] <= SOLVE_END_X and SOLVE_START_Y <= position[1] <= SOLVE_END_Y:
                    solver.click()
                    success = solver.solve()
                elif RESET_START_X <= position[0] <= RESET_END_X and RESET_START_Y <= position[1] <= RESET_END_Y:
                    reset.click()
                    reset.reset()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_TAB:
                    key = 0
                    (row, col) = grid.next(row, col)
                    grid.click(row, col)
                if event.key == pygame.K_1 or event.key == pygame.K_KP1:
                    key = 1
                    grid.input(row, col, key)
                if event.key == pygame.K_2 or event.key == pygame.K_KP2:
                    key = 2
                    grid.input(row, col, key)
                if event.key == pygame.K_3 or event.key == pygame.K_KP3:
                    key = 3
                    grid.input(row, col, key)
                if event.key == pygame.K_4 or event.key == pygame.K_KP4:
                    key = 4
                    grid.input(row, col, key)
                if event.key == pygame.K_5 or event.key == pygame.K_KP5:
                    key = 5
                    grid.input(row, col, key)
                if event.key == pygame.K_6 or event.key == pygame.K_KP6:
                    key = 6
                    grid.input(row, col, key)
                if event.key == pygame.K_7 or event.key == pygame.K_KP7:
                    key = 7
                    grid.input(row, col, key)
                if event.key == pygame.K_8 or event.key == pygame.K_KP8:
                    key = 8
                    grid.input(row, col, key)
                if event.key == pygame.K_9 or event.key == pygame.K_KP9:
                    key = 9
                    grid.input(row, col, key)
                if event.key == pygame.K_DELETE or event.key == pygame.K_BACKSPACE:
                    key = 0
                    grid.input(row, col, key)
                if event.key == pygame.K_s:
                    solver.gui_solve(0, 0, event)
        grid.check()

        # if (grid.solved()):
            # running = False

        redraw(screen, grid, solver, reset, play_time)

        pygame.display.update()
        # clock.tick(50)

        await asyncio.sleep(0)
        if not running:
            pygame.quit()
            return


if __name__ == "__main__":
    # game()
    asyncio.run(main())