import os
import pygame
from pywander.objects.base import ObjectBase


class LabelObject(ObjectBase):
    size = 12
    text = ''
    alias = 1
    color = (0, 0, 0)

    def __init__(self, text, size=12, color=(102, 102, 102), alias=1):
        self.text = text
        self.size = size
        self.color = color
        self.alias = alias

        self.recreate_surface_object()
        super(LabelObject, self).__init__()

    def set_color(self, color):
        self.color = color
        self.recreate_surface_object()

    def get_color(self):
        return self.color

    def recreate_surface_object(self):
        font = pygame.font.Font(os.path.join('data', 'fonts', 'Flames.ttf'), self.size)
        self.surface_to_draw = font.render(self.text, self.alias, self.color)
