import pygame

class Cell:
    dimension = 495
    
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.sketched_value = 0
        self.selected = None
        

    def set_cell_value(self, value):
        self.value = value

    def set_sketched_value(self, value):
        self.sketched_value = value

    def draw(self):
        width =  495
        height = 495
        smallFont = pygame.font.Font('freesansbold.ttf', 25)
        smallerFont = pygame.font.Font('freesansbold.ttf', 15)
        
        posX = (height/9)*(self.col)
        posY = (width/9)*(self.row)
        # implement along with gui
        
        if self.value != 0:
            text = smallFont.render(str(self.value), False, (0, 0, 0))
            self.screen.blit(text, (posX + 20, posY + 16))
        
        
        if self.sketched_value != 0 and self.value == 0:
            sketchText = smallerFont.render(str(self.sketched_value), False, (100, 100, 100))
            self.screen.blit(sketchText, (4 + posX + 2*(height/81 * (self.sketched_value % 4 )), 4 + posY + 3*(height/81 * (self.sketched_value // 4))))
            

        if self.selected == True:
    
            selection_box = pygame.Rect((Cell.dimension / 9 * (self.row)), (Cell.dimension / 9 * self.col), 55, 55)
            pygame.draw.rect(self.screen, (255, 0, 0), selection_box, width = 2)
        
    def select(self):
        self.selected = True
    
    def deselect(self):
        self.selected = False
    
    
            
            