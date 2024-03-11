import asyncio
import pygame
from src.game import game
from src.styles import SCREEN_COLOR, COLOR, BUTTON_COLOR
from src.classes.gui.grid import Grid
from src.classes.solver import Solver

pygame.font.init()
font = pygame.font.SysFont(None, 40)

SCREEN_WIDTH = 570
SCREEN_HEIGHT = 670
GRID_WIDTH = 540
GRID_HEIGHT = 540
GRID_OFFSET = 15
GRID_ROWS = 9
GRID_COLS = 9
CELL_WIDTH = GRID_WIDTH / GRID_COLS
CELL_HEIGHT = GRID_HEIGHT / GRID_ROWS
BUTTON_WIDTH = 100
BUTTON_HEIGHT = 75


async def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Sudoku")
    screen.fill(SCREEN_COLOR)
    clock = pygame.time.Clock()

    grid = Grid(screen, GRID_WIDTH, GRID_HEIGHT, GRID_OFFSET, GRID_ROWS, GRID_COLS)
    key = 0
    row = 0
    col = 0

    solve_text = font.render(str("Solve"), True, COLOR)
    solve_button = pygame.Rect(
      (SCREEN_WIDTH / 2) - BUTTON_WIDTH - GRID_OFFSET,
      GRID_HEIGHT + 2*GRID_OFFSET,
      BUTTON_WIDTH,
      BUTTON_HEIGHT
    )
    pygame.draw.rect(screen, BUTTON_COLOR, solve_button)
    screen.blit(solve_text, (solve_button.left + 15, solve_button.top + 25))

    running = True

    while(running):
        grid.draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos()
                if GRID_OFFSET <= position[0] <= (GRID_WIDTH + GRID_OFFSET) and GRID_OFFSET <= position[1] <=(GRID_HEIGHT + GRID_OFFSET):
                    x = position[0] - GRID_OFFSET
                    y = position[1] - GRID_OFFSET
                    row = int(y // CELL_HEIGHT)
                    col = int(x // CELL_WIDTH)
                    grid.click(row, col)
                else:
                    solver = Solver(grid)
                    solver.solve(0, 0)
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
        # if (grid.solved()):
            # running = False
        pygame.display.flip()
        clock.tick(50)

        await asyncio.sleep(0)
        if not running:
            pygame.quit()
            return


if __name__ == "__main__":
    # game()
    asyncio.run(main())
