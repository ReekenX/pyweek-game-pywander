from pywander.sprites.base import SpriteBase
from pywander.objects.image import ImageObject


class AsteroidSprite(SpriteBase):
    def __init__(self, *args, **kwargs):
        super(AsteroidSprite, self).__init__(*args, **kwargs)
        self.image = ImageObject('asteroid_1.png')

    def draw_on_surface(self, surface):
        self.image.rect.left -= 2
        super(AsteroidSprite, self).draw_on_surface(surface)
