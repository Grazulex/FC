import pygame

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 800
SCREEN_TITLE = 'Farmstead Chronicles'

class Screen:
    def __init__(self):
        self.canvas = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption(SCREEN_TITLE)

    def update(self, sprite, x, y):
        self.canvas.fill((255,255,255))
        self.canvas.blit(sprite, (x, y))
        self.window.blit(self.canvas, (0,0))
        pygame.display.update()
