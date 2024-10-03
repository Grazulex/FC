import pygame

from screen import Screen
from spritesheet import Spritesheet

class Main:
    def __init__(self):
        pygame.init()
        self.screen = Screen()
        self.running = True
        self.action = "idle"
        self.direction = "down"
        self.x = 0
        self.y = 0
        self.index = 0
        self.last_update = pygame.time.get_ticks()
        self.interval = 100

    def update(self):
        while self.running:
            ################################# CHECK PLAYER INPUT #################################
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        self.action = "run"
                        self.direction = "down"
                        self.y += 1
                    if event.key == pygame.K_LEFT:
                        self.action = "run"
                        self.direction = "left"
                        self.x = self.x - 1
                    if event.key == pygame.K_RIGHT:
                        self.action = "run"
                        self.direction = "right"
                        self.x = self.x + 1
                    if event.key == pygame.K_UP:
                        self.action = "run"
                        self.direction = "up"
                        self.y = self.y - 1
                    my_spritesheet = Spritesheet('player', self.action)
                    sprite = my_spritesheet.list_all_sprites(self.direction)
                    self.index = 0
                else:
                    self.action = "idle"

                    my_spritesheet = Spritesheet('player', self.action)
                    sprite = my_spritesheet.list_all_sprites(self.direction)
                    self.index = 0

            current_time = pygame.time.get_ticks()
            if current_time - self.last_update > self.interval:
                self.index = (self.index + 1) % len(sprite)
                self.last_update = current_time

            ################################# UPDATE WINDOW AND DISPLAY #################################
            self.screen.update(sprite[self.index], self.x, self.y)


if __name__ == '__main__':
    main = Main()
    main.update()