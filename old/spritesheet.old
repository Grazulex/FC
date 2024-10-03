from fileinput import filename

import pygame
import json

PATH_ASSETS = '../assets/sprites/'

class Spritesheet:
    def __init__(self, actor='player', action='idle'):
        self.filename = PATH_ASSETS+actor+'/'+action+'.png'
        self.sprite_sheet = pygame.image.load(self.filename).convert()
        self.meta_data = self.filename.replace('png', 'json')
        with open(self.meta_data) as f:
            self.data = json.load(f)
        f.close()

    def get_sprite(self, x, y, w, h):
        sprite = pygame.Surface((w, h))
        sprite.set_colorkey((0,0,0))
        sprite.blit(self.sprite_sheet,(0, 0),(x, y, w, h))
        return sprite

    def parse_sprite(self, name):
        sprite = self.data['frames'][name]['frame']
        x, y, w, h = sprite["x"], sprite["y"], sprite["w"], sprite["h"]
        image = self.get_sprite(x, y, w, h)
        return image

    def list_all_sprites(self, direction):
        direction_sprites = [name for name in self.data['frames'] if name.startswith(direction+'-')]
        walk_direction = []
        for sprite in direction_sprites:
            walk_direction.append(self.parse_sprite(sprite))
        return walk_direction