import pygame
from pywander.sprites.base import SpriteBase
from pywander.objects.image import ImageObject


class EnemySprite(SpriteBase):
    start_explosion = False
    explosion_frame = 0
    speed = 0.24
    time = 0
    x_position = 680

    def __init__(self, *args, **kwargs):
        super(EnemySprite, self).__init__(*args, **kwargs)
        self.image = ImageObject('enemy_ship.png')
        self.time = pygame.time.get_ticks()

    def draw_on_surface(self, surface):
        if not self.start_explosion:
            time_before = self.time
            self.time = pygame.time.get_ticks()
            elapsed = self.time - time_before
            self.x_position -= int(elapsed * self.speed)
            self.image.rect.left = int(self.x_position)
            super(EnemySprite, self).draw_on_surface(surface)
        else:
            if self.explosion_frame != 15:
                tmp_rect = self.image.rect
                self.image = ImageObject('explosion-%d.png' % self.explosion_frame)
                self.image.rect = tmp_rect
                self.explosion_frame += 1
                super(EnemySprite, self).draw_on_surface(surface)

    def show_explosion(self):
        self.start_explosion = True

    def is_completed(self):
        return self.explosion_frame == 15
