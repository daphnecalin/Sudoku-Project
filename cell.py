import pygame

class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.sketched_value = 0

    def set_cell_value(self, value):
        self.value = value

    def set_sketched_value(self, value):
        self.sketched_value = value

    def draw(self):
        width =  495
        height = 495
        smallFont = pygame.font.Font('freesansbold.ttf', 20)
        smallerFont = pygame.font.Font('freesansbold.ttf', 15)
        
        posX = (height/9)*(self.col)
        posY = (width/9)*(self.row)
        # implement along with gui
        
        if self.value != 0:
            text = smallFont.render(str(self.value), False, (0, 0, 0))
            self.screen.blit(text, (posX + 20, posY + 20))
        
        
        if self.sketched_value != 0:
            sketchText = smallerFont.render(str(self.sketched_value), False, (100, 100, 100))
            self.screen.blit(sketchText, (4 + posX + 2*(height/81 * (self.sketched_value % 4 )), 4 + posY + 3*(height/81 * (self.sketched_value // 4))))
        
            
            