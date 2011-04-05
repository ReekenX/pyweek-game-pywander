import pygame
from pywander.sprites.base import SpriteBase
from pywander.objects.image import ImageObject


class ShipSprite(SpriteBase):
    def __init__(self, *args, **kwargs):
        pygame.sprite.Sprite.__init__(self)
        self.image = ImageObject('ship.png')
