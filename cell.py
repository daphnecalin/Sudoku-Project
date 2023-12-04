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
        
        if value != 0:
            self.initial = True
        else:
            self.initial = False
        

    def set_cell_value(self, value):
        if not self.initial:
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
            # FIX THIS!
            x = posX + (height/81)*((self.value - 1) % 3)
            y = posY + (height/81)*((self.value - 1) % 3)
            self.screen.blit(sketchText, (x,y))
            

        if self.selected == True:
    
            selection_box = pygame.Rect((Cell.dimension / 9 * (self.col)), (Cell.dimension / 9 * self.row), 55, 55)
            pygame.draw.rect(self.screen, (255, 0, 0), selection_box, width = 2)
        
    def select(self):
        self.selected = True
    
    def deselect(self):
        self.selected = False
    
    def is_initial(self):
        return self.initial
    
    def get_row(self):
        return self.row
    
    def get_col(self):
        return self.col
    
            
            