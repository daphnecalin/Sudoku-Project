import pygame
from board import Board
from cell import Cell
from sudoku_generator import SudokuGenerator

pygame.init()
boardDimension = 495 # width and height of board

screen = pygame.display.set_mode([boardDimension+2, boardDimension+2]) # draw things relative to this
running = True
is_menu = True

pygame.display.set_caption('Sudoku')
cat = pygame.image.load('catbox.png')
bg = pygame.image.load('bg.jpg')

titleFont = pygame.font.Font('freesansbold.ttf', 50)
smallFont = pygame.font.Font('freesansbold.ttf', 20)




if __name__ == "__main__":
    running = True
    menu = True
    game = False
    difficulty = ""
    
    while running:
        while menu:
            btnWidth = 95
            btnHeight = 50
            btnPosX = 110
            btnPosY = 325
            
            mouse = pygame.mouse.get_pos()
            
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT:
                    running = False
                    menu = False
                    break
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if btnPosX < mouse[0] < btnPosX + btnWidth and btnPosY < mouse[1] < btnPosY + btnHeight:
                        difficulty = "easy"
                        print("ez")
                        game = True
                        menu = False
                        
                    elif (btnPosX + btnWidth < mouse[0] < btnPosX + 2*btnWidth) and (btnPosY <= mouse[1] <= btnPosY + btnHeight):
                        difficulty = "medium"
                        game = True
                        menu = False
                        
                    elif (btnPosX + 2*btnWidth < mouse[0] < btnPosX + 3*btnWidth) and (btnPosY <= mouse[1] <= btnPosY + btnHeight):
                        difficulty = "hard"
                        game = True
                        menu = False
                        

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
            
            
            pygame.draw.rect(screen, (125, 125, 125), pygame.Rect(btnPosX, btnPosY, btnWidth, btnHeight)) # left
            pygame.draw.rect(screen, (150, 150, 150), pygame.Rect(btnPosX + btnWidth, btnPosY, btnWidth, btnHeight)) # middle button
            pygame.draw.rect(screen, (125, 125, 125), pygame.Rect(btnPosX + (2*btnWidth), btnPosY, btnWidth, btnHeight)) # right
            
            easyButton = smallFont.render('Easy', False, (0, 0, 0))
            mediumButton = smallFont.render('Medium', False, (0, 0, 0))
            hardButton = smallFont.render('Hard', False, (0, 0, 0))
            
            
            screen.blit(easyButton, (btnPosX + 20, btnPosY + 15)) # offset of (20, 15)
            screen.blit(mediumButton, (216, 340)) # offset of (15, 15), simpler to hardcode...
            screen.blit(hardButton, (320, 340)) # offset of (20, 15)
            
            # hover effect
            if btnPosX < mouse[0] < btnPosX + btnWidth and btnPosY < mouse[1] < btnPosY + btnHeight:
                pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(btnPosX, btnPosY, btnWidth, btnHeight), width = 2) # left
                
            elif (btnPosX + btnWidth < mouse[0] < btnPosX + 2*btnWidth) and (btnPosY <= mouse[1] <= btnPosY + btnHeight):
                pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(btnPosX + btnWidth, btnPosY, btnWidth, btnHeight), width = 2)
                
            elif (btnPosX + 2*btnWidth < mouse[0] < btnPosX + 3*btnWidth) and (btnPosY <= mouse[1] <= btnPosY + btnHeight):
                pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(btnPosX + (2*btnWidth), btnPosY, btnWidth, btnHeight), width = 2) # right
            # when pressed: change_to_game()

            pygame.display.flip()
            
        
        while game:
            
            mouse = pygame.mouse.get_pos()
            
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT:
                    running = False
                    game = False
                    break
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # check for selecting cells
                    row = mouse[1] // (boardDimension // 9)
                    col = mouse[0] // (boardDimension // 9)
                    board.select(row, col)
                    pass
            
            board = Board(boardDimension, boardDimension, screen, difficulty)
            
            if difficulty == "easy":
                pass
            
            pygame.display.flip()
    
    pygame.quit()
    
    