import random
import pygame
from pywander.sprites.base import SpriteBase
from pywander.sprites.bullet import BulletSprite
from pywander.objects.image import ImageObject


class BossSprite(SpriteBase):
    moving_up = False
    life = 100

    last_fire_time = 0
    fire_time_delay = 1500
    hole = 1   
    pause_till = 0

    def __init__(self, *args, **kwargs):
        super(BossSprite, self).__init__(*args, **kwargs)
        self.image = ImageObject('boss.png')
        self.last_fire_time = pygame.time.get_ticks()

    def draw_on_surface(self, surface, game_board):
        if self.image.rect.left > 480:
            self.image.rect.left -= 1
            self.pause_till = pygame.time.get_ticks() + 4500

        if self.pause_till and self.pause_till < pygame.time.get_ticks():
            self.image.rect.left -= 1
            self.image.rect.top -= 1

            if self.image.rect.top < -self.image.rect.height:
                game_board.enemy_group.remove(self)
                game_board.attempts_left -= 1
        else:
            if self.moving_up:
                if self.image.rect.top > 0:
                    self.image.rect.top -= 1
                else:
                    self.moving_up = False
            else:
                if self.image.rect.top < 470 - self.image.rect.height:
                    self.image.rect.top += 1
                else:
                    self.moving_up = True

        if random.randint(1, 5) == 5:
            time_now = pygame.time.get_ticks()
            if self.last_fire_time + self.fire_time_delay < time_now:
                bullet = BulletSprite(False)
                bullet.image.rect.left = self.image.rect.left + self.image.rect.width / 2
                if self.hole == 1:
                    bullet.image.rect.top = self.image.rect.top + self.image.rect.height / 2 - 34
                    self.hole = 2
                else:
                    bullet.image.rect.top = self.image.rect.top + self.image.rect.height / 2 + 20
                    self.hole = 1
                bullet.rect = bullet.image.rect
                game_board.enemy_group.add(bullet)
                self.last_fire_time = time_now

        super(BossSprite, self).draw_on_surface(surface, game_board)

    def hit(self):
        self.life -= 4
