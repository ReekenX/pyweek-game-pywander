import pygame
from pywander.sprites.base import SpriteBase
from pywander.objects.image import ImageObject


class BulletSprite(SpriteBase):
    def __init__(self, from_ship=True, *args, **kwargs):
        pygame.sprite.Sprite.__init__(self)
        if from_ship:
            self.image = ImageObject('ship_bullet.png')
