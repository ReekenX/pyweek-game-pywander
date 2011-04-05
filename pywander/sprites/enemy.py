from pywander.sprites.base import SpriteBase
from pywander.objects.image import ImageObject


class EnemySprite(SpriteBase):
    start_explosion = False
    explosion_frame = 0

    def __init__(self, *args, **kwargs):
        super(EnemySprite, self).__init__(*args, **kwargs)
        self.image = ImageObject('enemy_ship.png')

    def draw_on_surface(self, surface):
        if not self.start_explosion:
            self.image.rect.left -= 1
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
