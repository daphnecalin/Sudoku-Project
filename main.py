import pygame
from board import Board
from cell import Cell
from sudoku_generator import SudokuGenerator

pygame.init()
boardDimension = 495 # width and height of board

screen = pygame.display.set_mode([boardDimension+2, boardDimension+52]) # draw things relative to this
running = True
is_menu = True

pygame.display.set_caption('Sudoku')
cat = pygame.image.load('catbox.png')
bg = pygame.image.load('bg.jpg')

titleFont = pygame.font.Font('freesansbold.ttf', 50)
smallFont = pygame.font.Font('freesansbold.ttf', 20)


def change_to_game(difficulty):
    board = Board(boardDimension, boardDimension, screen, difficulty)
    return True, board
    
def button_hover(btnPosX, btnPosY, btnWidth, btnHeight, x, y):
    # Create hover effect
    if btnPosX < x < btnPosX + btnWidth and btnPosY < y < btnPosY + btnHeight: # Check whether mouse is within dimensions of button
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(btnPosX, btnPosY, btnWidth, btnHeight), width = 2) # Draw red border around button
        
    elif (btnPosX + btnWidth < x < btnPosX + 2*btnWidth) and (btnPosY <= y <= btnPosY + btnHeight):
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(btnPosX + btnWidth, btnPosY, btnWidth, btnHeight), width = 2)
        
    elif (btnPosX + 2*btnWidth < x < btnPosX + 3*btnWidth) and (btnPosY <= y <= btnPosY + btnHeight):
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(btnPosX + (2*btnWidth), btnPosY, btnWidth, btnHeight), width = 2) # right

if __name__ == "__main__":
    running = True
    menu = True
    game = False
    difficulty = ""
    board = None
    
    btnWidth = 95
    btnHeight = 50
    btnPosX = 110
    
    
    while running:
        while menu:
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
                        game, board = change_to_game("easy")
                        menu = False
                        
                    elif (btnPosX + btnWidth < mouse[0] < btnPosX + 2*btnWidth) and (btnPosY <= mouse[1] <= btnPosY + btnHeight):
                        difficulty = "medium"
                        game, board = change_to_game("medium")
                        menu = False
                        
                    elif (btnPosX + 2*btnWidth < mouse[0] < btnPosX + 3*btnWidth) and (btnPosY <= mouse[1] <= btnPosY + btnHeight):
                        difficulty = "hard"
                        game, board = change_to_game("hard")
                        menu = False
                        

            # Set up screen, window text
            screen.fill((255, 255, 255))
            titleText = titleFont.render('Sudoku', False, (0, 0, 0))

            # Draw title text, background, and image
            screen.blit(bg, (0,0))
            pygame.draw.rect(screen, (255,255,255), pygame.Rect(110,80,290,250)) # hard-coded positions ..
            screen.blit(titleText, (160,100))
            screen.blit(cat, (195, 150))

            # Get mouse position each run
            mouse = pygame.mouse.get_pos() 
            
            # Draw buttons to choose difficulty
            pygame.draw.rect(screen, (125, 125, 125), pygame.Rect(btnPosX, btnPosY, btnWidth, btnHeight)) # left
            pygame.draw.rect(screen, (150, 150, 150), pygame.Rect(btnPosX + btnWidth, btnPosY, btnWidth, btnHeight)) # middle button
            pygame.draw.rect(screen, (125, 125, 125), pygame.Rect(btnPosX + (2*btnWidth), btnPosY, btnWidth, btnHeight)) # right
            
            # Store text to be displayed on buttons
            easyButton = smallFont.render('Easy', False, (0, 0, 0))
            mediumButton = smallFont.render('Medium', False, (0, 0, 0))
            hardButton = smallFont.render('Hard', False, (0, 0, 0))
            
            # Render text onto buttons
            screen.blit(easyButton, (btnPosX + 20, btnPosY + 15)) # offset of (20, 15)
            screen.blit(mediumButton, (216, 340)) # offset of (15, 15), simpler to hardcode...
            screen.blit(hardButton, (320, 340)) # offset of (20, 15)
            
            # Create hover effect
            button_hover(btnPosX, btnPosY, btnWidth, btnHeight, mouse[0], mouse[1])
            # when pressed: change_to_game()

            pygame.display.flip() # Update display
            
        
        while game:
            btnPosY = 497
            original_board = board
            # Get mouse each frame
            mouse = pygame.mouse.get_pos()
            
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT:
                    running = False
                    game = False
                    break
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Check for selecting cells
                    location = board.click(mouse[0], mouse[1])
                    if location:
                        row, col = location
                        
                        board.select(row, col)
                    
                    if btnPosX < mouse[0] < btnPosX + btnWidth and btnPosY < mouse[1] < btnPosY + btnHeight: # reset button functionality
                        board.reset_to_original()
                        
                    elif (btnPosX + btnWidth < mouse[0] < btnPosX + 2*btnWidth) and (btnPosY <= mouse[1] <= btnPosY + btnHeight): # restart button
                        board = Board(boardDimension, boardDimension, screen, difficulty)
                        
                    elif (btnPosX + 2*btnWidth < mouse[0] < btnPosX + 3*btnWidth) and (btnPosY <= mouse[1] <= btnPosY + btnHeight): # exit game
                        game = False
                        running = False
                        
                if event.type == pygame.KEYDOWN and event.unicode.isdigit():
                    print(int(event.unicode))
                    board.sketch(int(event.unicode))
                    
                if event.type == pygame.KEYDOWN:
                    pass
            
            
            
            board.draw()
            
            # Draw buttons to control game
            pygame.draw.rect(screen, (113, 216, 84), pygame.Rect(btnPosX, btnPosY, btnWidth, btnHeight)) # reset
            pygame.draw.rect(screen, (34, 191, 81), pygame.Rect(btnPosX + btnWidth, btnPosY, btnWidth, btnHeight)) # restart
            pygame.draw.rect(screen, (113, 216, 84), pygame.Rect(btnPosX + (2*btnWidth), btnPosY, btnWidth, btnHeight)) # right
            
            # Store text to be displayed on buttons
            resetButton = smallFont.render('Reset', False, (0, 0, 0))
            restartButton = smallFont.render('Restart', False, (0, 0, 0))
            exitButton = smallFont.render('Exit', False, (0, 0, 0))
            
            # Render text onto buttons
            screen.blit(resetButton, (btnPosX + 20, btnPosY + 15)) # offset of (20, 15)
            screen.blit(restartButton, (btnPosX + btnWidth + 15, btnPosY + 15)) # offset of (15, 15), simpler to hardcode...
            screen.blit(exitButton, (btnPosX + btnWidth*2 + 20, btnPosY + 15)) # offset of (20, 15)
            
            
         # Create hover effect
            button_hover(btnPosX, btnPosY, btnWidth, btnHeight, mouse[0], mouse[1])
            
            
            
            
            # Redraw display
            pygame.display.flip()
    
    pygame.quit()
    
    