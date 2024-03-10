import pygame
from game import game

pygame.font.init()

SCREEN_WIDTH = 570
SCREEN_HEIGHT = 670
GRID_WIDTH = 540
GRID_HEIGHT = 540
GRID_OFFSET = 15
GRID_ROWS = 9
GRID_COLS = 9

BUTTON_WIDTH = 100
BUTTON_HEIGHT = 75


def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Sudoku")
    screen.fill("#323232")
    clock = pygame.time.Clock()

    running = True

    while(running):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.flip()
        clock.tick(50)

    pygame.quit()


if __name__ == "__main__":
    # game()
    main()
