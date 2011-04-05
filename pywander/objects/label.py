import pygame
from pywander.objects.base import ObjectBase


class LabelObject(ObjectBase):
    name = None
    size = 12
    text = ''
    alias = 1
    color = (0, 0, 0)

    def __init__(self, text, name=None, size=12, color=(0, 0, 0), alias=1):
        self.text = text
        self.name = name
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
        font = pygame.font.SysFont(self.name, self.size, True)
        self.surface_to_draw = font.render(self.text, self.alias, self.color)
