from pywander.sprites.base import SpriteBase
from pywander.objects.image import ImageObject


class BossSprite(SpriteBase):
    def __init__(self, *args, **kwargs):
        super(BossSprite, self).__init__(*args, **kwargs)
        self.image = ImageObject('boss.png')

    def draw_on_surface(self, surface):
        self.image.rect.left -= 1
        super(BossSprite, self).draw_on_surface(surface)
