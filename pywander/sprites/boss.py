from pywander.sprites.base import SpriteBase
from pywander.objects.image import ImageObject


class BossSprite(SpriteBase):
    moving_up = False

    def __init__(self, *args, **kwargs):
        super(BossSprite, self).__init__(*args, **kwargs)
        self.image = ImageObject('boss.png')

    def draw_on_surface(self, surface):
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

        super(BossSprite, self).draw_on_surface(surface)
