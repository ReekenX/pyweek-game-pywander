import random
import pygame
from pywander.sprites.base import SpriteBase
from pywander.sprites.bullet import BulletSprite
from pywander.objects.image import ImageObject


class EnemySprite(SpriteBase):
    start_explosion = False
    explosion_frame = 0
    speed = 0.24
    time = 0
    x_position = 680

    last_fire_time = 0
    fire_time_delay = 2500

    def __init__(self, *args, **kwargs):
        super(EnemySprite, self).__init__(*args, **kwargs)
        self.image = ImageObject('enemy_ship.png')
        self.time = pygame.time.get_ticks()

    def draw_on_surface(self, surface, game_board):
        if not self.start_explosion:
            time_before = self.time
            self.time = pygame.time.get_ticks()
            elapsed = self.time - time_before
            self.x_position -= int(elapsed * self.speed)
            self.image.rect.left = int(self.x_position)

            if random.randint(1, 6) == 6:
                time_now = pygame.time.get_ticks()
                if self.last_fire_time + self.fire_time_delay < time_now:
                    bullet = BulletSprite(False)
                    bullet.image.rect.left = self.image.rect.left + self.image.rect.width / 2 - 4
                    bullet.image.rect.top = self.image.rect.top + self.image.rect.height / 2 - 9
                    bullet.rect = bullet.image.rect
                    game_board.enemy_group.add(bullet)
                    self.last_fire_time = time_now

            super(EnemySprite, self).draw_on_surface(surface, game_board)
        else:
            if self.explosion_frame != 15:
                tmp_rect = self.image.rect
                self.image = ImageObject('explosion-%d.png' % self.explosion_frame)
                self.image.rect = tmp_rect
                self.explosion_frame += 1
                super(EnemySprite, self).draw_on_surface(surface, game_board)

    def show_explosion(self):
        self.start_explosion = True

    def is_completed(self):
        return self.explosion_frame == 15 or self.x_position <= -self.image.rect.width
