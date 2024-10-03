import pygame

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 800
SCREEN_TITLE = 'Farmstead Chronicles'

class Screen:
    def __init__(self):
        self.display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption(SCREEN_TITLE)
        self.clock: pygame.time.Clock = pygame.time.Clock()
        self.frameRate: int = 144
        self.deltatime: float = 0.0

    def update(self):
        pygame.display.flip()
        pygame.display.update()
        self.clock.tick(self.frameRate)
        self.display.fill((0, 0, 0))
        self.deltatime = self.clock.get_time()

    def get_delta_time(self):
        return self.deltatime

    def get_size(self):
        return self.display.get_size()

    def get_display(self):
        return self.display

