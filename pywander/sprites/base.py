import pygame
from pywander.objects.image import ImageObject


class SpriteBase(pygame.sprite.Sprite):
    def __init__(self, *args, **kwargs):
        super(self, SpriteBase).__init__(*args, **kwargs)
        self.image = ImageObject('ship.png')
