from pywander.sprites.base import SpriteBase
from pywander.objects.image import ImageObject


class BulletSprite(SpriteBase):
    def __init__(self, from_ship=True, *args, **kwargs):
        super(BulletSprite, self).__init__(*args, **kwargs)
        if from_ship:
            self.image = ImageObject('ship_bullet.png')
