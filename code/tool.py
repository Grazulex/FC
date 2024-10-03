import pygame


class Tool:

    @staticmethod
    def split_image(sprite_sheet : pygame.Surface, x: int, y:int, width: int, height: int):
        return sprite_sheet.subsurface(pygame.Rect(x, y, width, height))