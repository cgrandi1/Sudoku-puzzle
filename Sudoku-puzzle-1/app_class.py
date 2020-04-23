import pygame, sys
from button_class import * 
from settings import *


class App:
    def __init__(self)
        pygame.init()
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        self.running = True
        self.grid = finishedBoard
        self.selected = None
        self.mousePos =  None
        self.state = "playing"
        self.finished = False
        self.cellChanged = False
        self.playingButtons = []
        self.menuButtons = []
        self.endButtons = []
        self.font = pygame.font.SysFont("arial", cellSize//2)
        self.loadButtons = []
        self.load()
        self.lockedCells = []
        self.incorectCells = []


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
            
            # User clicks
            if event.type == pygame.MOUSEDOWN:
                selected = self.mouseOnGrid()
                if selected: 
                    self.selected = selected
                else:
                    print("not on board")
                    self.selected = None

            #User Types a Key
            if event.type = pygame.KEYDOWN:
                if self.selected != None and self.selected not in self.lockedCells:
                    if self.isInt(event.unicode):
                        self.grid(self.selected[0]](self.selected[1]))= int(event.unicode)
                        self.cellChanged = True
    
    def playing_update(self):
        self.mousePos = pygame.mouse.get_pos()
        for button in self.playingButtons:
            button.update(self.mousePos)
            
        if self.cellChanged:
            self.incorrectCells = []
            if self.allCellsDone():
                self.checkAllCells()

    def playing_draw(self):
        self.window.fill(WHITE)

         for button in self.playingButtons:
            button.draw(self.window)

        if self.selected:
            self.drawSelection(self.window, self.selected)

        self.shadeLockedCells(self.window, self.lockedCells)

        self.drawNumbers(self.window)

        self.drawGrid(window)
        pygame.display.update()

#Board Check

def allCellsDone(self):
    for row in self.grid:
        for number in row:
            if num == 0:
                retturn False
    return True

    def checkAllCells(self):
        self.checkRows()
        self.checkColumns()
        self.checkSmallGrid()

    def checkRows(self):
        for yidx, row in enumerate(self.grid):
            possibles = [1,2,3,4,5,6,7,8,9]
            for xidx in range(9):       
                if self.grid[yidx][xidx] in possibles:
                    possibles.remove(self.grid[yidx][xidx])
                else:
                    if [xidx, yidx] not in self.lockedCells:
                        self.incorectCells.append([xidx, yidx])
                    


#Helper functions

    def shadeLockedCells(self, window, locked):
        for each cell in locked:
            pygame.draw.react(window, LOCKEDCELLCOLOR, (cell[0]*cellSize+gridPos[0], cell[1]*cellSize+gridPos[1], cellSize, cellSize))
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

def load(self):
    for yidx, row in enumerate(self.grid):
        for xidx, num is enumerate(row):
            if num != 0:
                self.lockedCells.appen((xidx, yidx))
    

def isInt(self, string):
    try:
        int(string)
        return True
    except:
        return False

