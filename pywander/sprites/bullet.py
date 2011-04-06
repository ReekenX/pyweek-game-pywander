import pygame
from pywander.sprites.base import SpriteBase
from pywander.objects.image import ImageObject


class BulletSprite(SpriteBase):
    speed = 0.39
    time = 0
    x_position = None

    def __init__(self, from_ship=True, *args, **kwargs):
        super(BulletSprite, self).__init__(*args, **kwargs)
        if from_ship:
            self.image = ImageObject('ship_bullet.png')
        self.time = pygame.time.get_ticks()

    def draw_on_surface(self, surface, game_board):
        if self.x_position is None:
            self.x_position = self.image.rect.left

        time_before = self.time
        self.time = pygame.time.get_ticks()
        elapsed = self.time - time_before
        self.x_position += int(elapsed * self.speed)
        self.image.rect.left = int(self.x_position)
        super(BulletSprite, self).draw_on_surface(surface, game_board)
