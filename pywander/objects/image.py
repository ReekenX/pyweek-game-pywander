import os
import pygame
from pywander.objects.base import ObjectBase


class ImageObject(ObjectBase):
    def __init__(self, file_name):
        full_path = os.path.join('data', 'images', file_name)
        self.surface_to_draw = pygame.image.load(full_path)
        super(ImageObject, self).__init__()
