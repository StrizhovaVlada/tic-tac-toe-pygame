import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 600, 600
LINE_COLOR = (0, 0, 0)
BG_COLOR = (255, 255, 255)
LINE_WIDTH = 10

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Крестики-нолики")


def draw_board(screen):
    """Отрисовка линий игрового поля 3x3"""
    width, height = screen.get_size()
    cell_size = width // 3

    pygame.draw.line(screen, LINE_COLOR, (cell_size, 0), (cell_size, height), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (cell_size * 2, 0), (cell_size * 2, height), LINE_WIDTH)

    pygame.draw.line(screen, LINE_COLOR, (0, cell_size), (width, cell_size), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, cell_size * 2), (width, cell_size * 2), LINE_WIDTH)


def main():
    running = True

    while running:
        screen.fill(BG_COLOR)         
        draw_board(screen)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
