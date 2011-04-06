import pygame
from pywander.sprites.base import SpriteBase
from pywander.objects.image import ImageObject


class AsteroidSprite(SpriteBase):
    speed = 0.34
    time = 0
    x_position = 680

    def __init__(self, *args, **kwargs):
        super(AsteroidSprite, self).__init__(*args, **kwargs)
        self.image = ImageObject('asteroid_1.png')
        self.time = pygame.time.get_ticks()

    def draw_on_surface(self, surface, game_board):
        self.image.rect.left -= 2
        time_before = self.time
        self.time = pygame.time.get_ticks()
        elapsed = self.time - time_before
        self.x_position -= int(elapsed * self.speed)
        self.image.rect.left = int(self.x_position)
        super(AsteroidSprite, self).draw_on_surface(surface, game_board)
