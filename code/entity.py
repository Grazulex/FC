import pygame

from screen import Screen
from tool import Tool
from keylistener import KeyListener

class Entity(pygame.sprite.Sprite):

    def __init__(self, keylistener: KeyListener, screen: Screen, x: int, y: int):
        super().__init__()
        self.screen = screen
        self.keylistener = keylistener
        self.sprite_sheet = pygame.image.load("../assets/sprite/Base Character - Premium/basic/walk.png")
        self.image = Tool.split_image(self.sprite_sheet,0,0, 80, 80)
        self.position: pygame.math.Vector2 = pygame.math.Vector2(x + 16, y + 16)
        self.rect: pygame.Rect = self.image.get_rect()
        self.all_images = self.get_all_images()
        self.index_image = 0
        self.image_part = 0
        self.reset_animation = False
        self.hitbox: pygame.Rect = pygame.Rect(0, 0, 16, 16)
        self.step: int = 0
        self.animation_walk: bool = False
        self.direction = "down"

        self.animation_step_time: float = 0.0
        self.action_animation = 16

    def update(self):
        self.animation_sprite()
        self.move()
        self.rect.center = self.position
        self.hitbox.midbottom = self.rect.midbottom
        self.image = self.all_images[self.direction][self.index_image]

    def move_left(self):
        self.animation_walk = True
        self.direction = "left"

    def move_right(self):
        self.animation_walk = True
        self.direction = "right"

    def move_up(self):
        self.animation_walk = True
        self.direction = "up"

    def move_down(self):
        self.animation_walk = True
        self.direction = "down"

    def animation_sprite(self):
        if int(int(self.step // 8) + self.image_part) >= 8:
            self.image_part = 0
            self.reset_animation = True
        self.index_image = int(self.step // 8) + self.image_part

    def move(self):
        if self.animation_walk:
            self.animation_step_time += self.screen.get_delta_time()
            if self.step < 16 and self.animation_step_time >= self.action_animation:
                self.step += 1
                if self.direction == "left":
                    self.position.x -= 1
                elif self.direction == "right":
                    self.position.x += 1
                elif self.direction == "down":
                    self.position.y += 1
                elif self.direction == "up":
                    self.position.y -= 1
                self.animation_step_time = 0
            elif self.step >= 16:
                self.step = 0
                self.animation_walk = False
                if self.reset_animation:
                    self.reset_animation = False
                else:
                    if self.image_part == 0:
                        self.image_part = 4
                    else:
                        self.image_part = 0

    def align_hitbox(self):
        self.rect.center = self.position
        self.hitbox.midbottom = self.rect.midbottom
        while self.hitbox.x % 16 != 0:
            self.rect.x -= 1
            self.hitbox.midbottom = self.rect.midbottom
        while self.hitbox.y % 16 != 0:
            self.rect.y -= 1
            self.hitbox.midbottom = self.rect.midbottom
        self.position = pygame.math.Vector2(self.rect.center)

    def get_all_images(self):
        all_images = {
            "right" : [],
            "left" : [],
            "down": [],
            "up": []
        }

        width: int = self.sprite_sheet.get_width() // 8
        height: int = self.sprite_sheet.get_height() // 4

        for i in range(8):
            for j, key in enumerate(all_images.keys()):
                all_images[key].append(Tool.split_image(self.sprite_sheet,i*width,j*height, width, height))
        return all_images