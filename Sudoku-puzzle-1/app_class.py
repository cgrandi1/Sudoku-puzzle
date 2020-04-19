import pygame, sys
from settings import *

class App:
    def __init__(self)
        pygame.init()
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        self.running = True
        self.grid = testBoard
        print(self.grid)


    def run(self):
        while self.running:
            self.events()
            self.update()
            self.draw()
        pygame.quit()
        sys.exit()

    def events():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = FALSE

    
    def update(self):
        pass


    def draw(self):
        self.window.fill(WIDTH)
        self.drawGrid(window)
        pygame.display.update()

    def drawGrid(self):
        pygame.draw.react(window, BLACK, (gridPos[0], gridPos[1], WIDTH-40, HEIGHT-120))

