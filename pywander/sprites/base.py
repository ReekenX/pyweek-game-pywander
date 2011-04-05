import pygame
from pywander.objects.image import ImageObject


class SpriteBase(pygame.sprite.Sprite):
    def __init__(self, *args, **kwargs):
        super(SpriteBase, self).__init__(*args, **kwargs)
        self.image = ImageObject('ship.png')
        self.rect = self.image.rect

    def draw_on_surface(self, surface):
        self.image.draw_on_surface(surface)
        self.rect = self.image.rect
