from pywander.sprites.base import SpriteBase
from pywander.objects.image import ImageObject


class ShipSprite(SpriteBase):
    def __init__(self, *args, **kwargs):
        super(ShipSprite, self).__init__(*args, **kwargs)
        self.image = ImageObject('ship.png')
