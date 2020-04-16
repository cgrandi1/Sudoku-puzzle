import pygame
from settings import *

class App
    def __init__(self)
        pygame.init()
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        self.running = True

    def run(self):
        while self.running:
            self.events()
            self.update()
            self.draw()

    def events():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = FALSE