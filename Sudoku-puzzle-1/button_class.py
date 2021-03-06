import pygame

class Button:
    def __init__(self, x, y, width, height, text-None, color=(73, 73, 73), highlightedColor=(189, 189, 189) function=None, params=None):
        self.image = pygame.Surace((width, height))
        self.pos = (x, y
        self.rectangle = self.image.get_rectangle()
        self.rectangle.topleft = self.pos
        self.text = text
        self.color = color
        self.highlightedColor = highlightedColor
        self.function = function
        self.params = params
        self.highlighted = False
    
    def update(self, mouse):
        if self.rectangle.collidepoint(mouse):
            self.highlighted = True
        else:
            self.highlightedColor = False
    
    def draw(self, window):
        self.image.fill(self.highlightedColor if self.highlighted else self.color)
        window.blit(self.image, self.pos)

