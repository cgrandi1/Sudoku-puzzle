import pygame, sys
from button_class import * 
from settings import *


class App:
    def __init__(self)
        pygame.init()
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        self.running = True
        self.grid = testBoard2
        self.selected = None
        self.mousePos =  None
        self.state = "playing"
        self.playingButtons = []
        self.menuButtons = []
        self.endButtons = []
        self.font = pygame.font.SysFont("arial", cellSize//2)
        self.loadButtons = []


    def run(self):
        while self.running:
            if self.state == "playing":
                self.playing_events()
                self.playing_update()
                self.playing_draw()
        pygame.quit()
        sys.exit()
    

    def playing_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = FALSE
            if event.type == pygame.MOUSEDOWN:
                selected = self.mouseOnGrid()
                if selected: 
                    self.selected = selected
                else:
                    print("not on board")
                    self.selected = None
    
    def playing_update(self):
        self.mousePos = pygame.mouse.get_pos()
        for button in self.playingButtons:
            button.update(self.mousePos)

    def playing_draw(self):
        self.window.fill(WHITE)

         for button in self.playingButtons:
            button.draw(self.window)

        if self.selected:
            self.drawSelection(self.window, self.selected)

        self.drawNumbers(self.window)

        self.drawGrid(window)
        pygame.display.update()

#Helper functions

    def drawNumber(self, window):
        for yidx, row in enumerate(self.grid):
            for xidx, num in enumerate(row):
                if num !=0:
                    pos = [(xidx*cellSize)+gridPos[0], (y*cellSize)+gridPos[1]]
                    self.textToScreen(window, str(num), pos)

    def drawSelection(self, window, pos):
        pygame.draw.rectangle(window, LIGHTBLUE, ((pos[0]*cellSize], (pos[1]*cellSize)+gridPos[1], cellSize, cellSize ))

    def drawGrid(self):
        pygame.draw.rectangle(window, BLACK, (gridPos[0], gridPos[1], WIDTH-150, HEIGHT-150), 2)
        for x in range(9):
                pygame.draw.line(window, BLACK, (gridPos[0]+(x*cellSize), gridPos[1]), (gridPos[0]+(x*cellSize), gridPos[1]+450), 2 if x % 3 == 0 else x)
                pygame.draw.line(window, BLACK, (gridPos[0]+(x*cellSize), gridPos[1]+(x*cellSize)), (gridPos[0]+450, gridPos[1]++(x*cellSize)), 2 if x % 3 == 0 else x)
    

def mouseOnGrid(self):
    if self.mousePos[0] < gridPos[0] or self.mousePos[1] < gridPos[1]:
        return False
    if self.mousePos[0] > gridPos[0]+gridSize or self.mousePos[1] > gridPos[1]+gridSize:
        return False
    return ((self.mousePos[0]-gridPos[0]//cellSize, (self.mousePos(1)-gridPos[1])//cellSize)
    
def loadButtons(self):
    self.playingButtons.append(Button(20, 40, 100, 40))

def textToScreen(self, window, text, pos):
    font = self.font.render(text, False, BLACK)
    fontWidth = font.get_width()
    fontHeight = font.get_height()
    pos[0] += (cellSize-fontWidth)//2
    pos[1] += (cellSize-fontHeight)//2
    window.blit(font, pos)


