import pygame
# from board import Board
from cell import Cell
from sudoku_generator import SudokuGenerator

pygame.init()

screen = pygame.display.set_mode([512, 512]) # draw things relative to this
running = True
is_menu = True

def menu(): # main menu loop
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            return False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pass

    screen.fill((255, 255, 255))
    titleFont = pygame.font.Font('freesansbold.ttf', 50)
    titleText = titleFont.render('Sudoku', False, (0, 0, 0))

    screen.blit(titleText, (100,100))

    pygame.display.flip()
    return True # .............



def change_to_menu(): # cause menu to be displayed and initialize parts
    is_menu = True
    pass

def change_to_game(): # cause game to be displayed and initialize
    is_menu = False
    pass

def game(): # main game loop
    
    # implement when Board, Cell, SudokuGenerator are finished
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
            

    screen.fill((255, 255, 255))

    
    pygame.display.flip() # update screen


    return True

if __name__ == "__main__":
    while running:
        
        if is_menu:
            running = menu() # cursed
        else:
            running = game()

    pygame.quit()
    