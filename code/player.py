import pygame

from keylistener import KeyListener
from screen import Screen
from entity import Entity

class Player(Entity):
    def __init__(self, keylistener: KeyListener, screen: Screen, x: int, y: int):
        super().__init__(keylistener, screen, x, y)

        self.pokedollars = 0

    def update(self):
        self.check_move()
        super().update()


    def check_move(self):
        if self.animation_walk is False:
            if self.keylistener.key_pressed(pygame.K_LEFT):
                self.move_left()
            if self.keylistener.key_pressed(pygame.K_RIGHT):
                self.move_right()
            if self.keylistener.key_pressed(pygame.K_UP):
                self.move_up()
            if self.keylistener.key_pressed(pygame.K_DOWN):
                self.move_down()