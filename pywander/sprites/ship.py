import pygame
from pywander.sprites.base import SpriteBase
from pywander.sprites.bullet import BulletSprite
from pywander.objects.image import ImageObject


class ShipSprite(SpriteBase):
    ship_speed = 1.99
    ship_top = 180.00
    ship_left = 30.00

    last_fire_time = 0
    fire_delay = 1020

    def __init__(self, *args, **kwargs):
        super(ShipSprite, self).__init__(*args, **kwargs)
        self.image = ImageObject('ship.png')

    def move_ship_down(self):
        if self.image.rect.top + self.ship_speed < 401:
            self.ship_top += self.ship_speed

    def move_ship_up(self):
        if self.image.rect.top - self.ship_speed > 35:
            self.ship_top -= self.ship_speed

    def move_ship_left(self):
        if self.image.rect.left - self.ship_speed > 10:
            self.ship_left -= self.ship_speed

    def move_ship_right(self):
        if self.image.rect.left + self.ship_speed < 580:
            self.ship_left += self.ship_speed

    def draw_on_surface(self, surface, game_board):
        self.image.rect.top = int(self.ship_top)
        self.image.rect.left = int(self.ship_left)
        super(ShipSprite, self).draw_on_surface(surface, game_board)

    def fire_bullet(self, bullets_group):
        time_now = pygame.time.get_ticks()
        if self.last_fire_time + self.fire_delay < time_now:
            bullet = BulletSprite()
            bullet.image.rect.left = self.image.rect.left + self.image.rect.width / 2
            bullet.image.rect.top = self.image.rect.top + (self.image.rect.height / 2 - 9)
            bullets_group.add(bullet)
            self.last_fire_time = time_now
