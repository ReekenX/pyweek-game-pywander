import pygame
from pywander.sprites.base import SpriteBase
from pywander.objects.image import ImageObject


class BulletSprite(SpriteBase):
    speed = 0.39
    time = 0
    x_position = None
    is_ship_bullet = True

    def __init__(self, is_ship_bullet=True, *args, **kwargs):
        super(BulletSprite, self).__init__(*args, **kwargs)
        self.image = ImageObject('ship_bullet.png')
        self.is_ship_bullet = is_ship_bullet
        if not self.is_ship_bullet:
            self.image.surface_to_draw = pygame.transform.flip(self.image.surface_to_draw, True, False)
        self.time = pygame.time.get_ticks()

    def draw_on_surface(self, surface, game_board):
        if self.x_position is None:
            self.x_position = self.image.rect.left

        time_before = self.time
        self.time = pygame.time.get_ticks()
        elapsed = self.time - time_before
        if self.is_ship_bullet:
            self.x_position += int(elapsed * self.speed)
        else:
            self.x_position -= int(elapsed * self.speed)
        self.image.rect.left = int(self.x_position)
        super(BulletSprite, self).draw_on_surface(surface, game_board)
