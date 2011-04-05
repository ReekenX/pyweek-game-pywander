from pywander.sprites.base import SpriteBase
from pywander.objects.image import ImageObject


class EnemySprite(SpriteBase):
    def __init__(self, *args, **kwargs):
        super(EnemySprite, self).__init__(*args, **kwargs)
        self.image = ImageObject('enemy_ship.png')

    def draw_on_surface(self, surface):
        self.image.rect.left -= 1
        super(EnemySprite, self).draw_on_surface(surface)
