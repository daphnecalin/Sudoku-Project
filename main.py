import pygame
from board import Board
from cell import Cell
from sudoku_generator import SudokuGenerator

pygame.init()

def main():
    screen = pygame.display.set_mode([512, 512])
    running = True

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((255, 255, 255))


    pygame.quit()

if __name__ == "__main__":
    main()