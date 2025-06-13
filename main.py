import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 600, 600
LINE_COLOR = (0, 0, 0)
BG_COLOR = (255, 255, 255)
LINE_WIDTH = 10
CELL_SIZE = WIDTH // 3

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Крестики-нолики")


def draw_board(screen):
    """Отрисовка линий игрового поля 3x3"""
    width, height = screen.get_size()

    pygame.draw.line(screen, LINE_COLOR, (CELL_SIZE, 0), (CELL_SIZE, height), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (CELL_SIZE * 2, 0), (CELL_SIZE * 2, height), LINE_WIDTH)

    pygame.draw.line(screen, LINE_COLOR, (0, CELL_SIZE), (width, CELL_SIZE), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, CELL_SIZE * 2), (width, CELL_SIZE * 2), LINE_WIDTH)


def draw_x_o(row, col, player):
    """Отрисовка крестика или нолика в заданной ячейке"""
    center_x = col * CELL_SIZE + CELL_SIZE // 2
    center_y = row * CELL_SIZE + CELL_SIZE // 2
    if player == "X":
        offset = 20
        pygame.draw.line(screen, (255, 0, 0), (center_x - offset, center_y - offset), (center_x + offset, center_y + offset), 10)
        pygame.draw.line(screen, (255, 0, 0), (center_x + offset, center_y - offset), (center_x - offset, center_y + offset), 10)
    elif player == "O":
        pygame.draw.circle(screen, (0, 0, 255), (center_x, center_y), 25, 10)


def check_winner(board):
    """Проверка победителя: возвращает 'X', 'O' или None"""
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] is not None:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] is not None:
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        return board[0][2]
    return None


def main():
    board = [[None for _ in range(3)] for _ in range(3)]
    current_player = "X"
    running = True

    while running:
        screen.fill(BG_COLOR)
        draw_board(screen)

        for row in range(3):
            for col in range(3):
                if board[row][col] is not None:
                    draw_x_o(row, col, board[row][col])

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                row = y // CELL_SIZE
                col = x // CELL_SIZE

                if board[row][col] is None:
                    board[row][col] = current_player
                    winner = check_winner(board)
                    if winner:
                        print(f"Победитель: {winner}")
                        running = False
                    else:
                        if all(all(cell is not None for cell in row_cells) for row_cells in board):
                            print("Ничья!")
                            running = False
                        else:
                            current_player = "O" if current_player == "X" else "X"

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()