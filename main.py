import pygame
# from board import Board
from cell import Cell
from sudoku_generator import SudokuGenerator

pygame.init()

screen = pygame.display.set_mode([512, 512]) # draw things relative to this
running = True
is_menu = True

pygame.display.set_caption('Sudoku')
cat = pygame.image.load('catbox.png')
bg = pygame.image.load('bg.jpg')

titleFont = pygame.font.Font('freesansbold.ttf', 50)
smallFont = pygame.font.Font('freesansbold.ttf', 20)

print(pygame.font.get_fonts())
def menu(): # main menu loop
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            return False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pass

    # Set up screen, window text
    screen.fill((255, 255, 255))
    titleText = titleFont.render('Sudoku', False, (0, 0, 0))

    # Draw title text, background, and image
    screen.blit(bg, (0,0))
    pygame.draw.rect(screen, (255,255,255), pygame.Rect(110,80,290,250)) # hard-coded positions ..
    screen.blit(titleText, (160,100))
    screen.blit(cat, (195, 150))

    # Draw buttons and get click
    mouse = pygame.mouse.get_pos() 
    
    btnWidth = 95
    btnHeight = 50
    
    pygame.draw.rect(screen, (150, 150, 150), pygame.Rect(205, 325, btnWidth, btnHeight)) # middle button
    pygame.draw.rect(screen, (125, 125, 125), pygame.Rect(110, 325, btnWidth, btnHeight)) # left
    pygame.draw.rect(screen, (125, 125, 125), pygame.Rect(300, 325, btnWidth, btnHeight)) # right
    
    easyButton = smallFont.render('Easy', False, (0, 0, 0))
    mediumButton = smallFont.render('Medium', False, (0, 0, 0))
    hardButton = smallFont.render('Hard', False, (0, 0, 0))
    
    
    screen.blit(easyButton, (130, 340)) # offset of (20, 15)
    screen.blit(mediumButton, (216, 340)) # offset of (15, 15)
    screen.blit(hardButton, (320, 340)) # offset of (20, 15)
    
    # finish implementing clicks

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
    