import pygame
from pygame.locals import KEYDOWN
from pywander.boards.base import BoardBase
from pywander.boards.switch import SwitchBoard
from pywander.boards.game import GameBoard
from pywander.objects.label import LabelObject
from pywander.objects.image import ImageObject


class HowToBoard(BoardBase):
    switch_board = False
    objects = []

    def __init__(self, *args, **kwargs):
        self.background = ImageObject('background.png')

    def process_draw_on_surface(self, surface):
        self.background.draw_on_surface(surface)

        if self.objects == []:
            label = LabelObject('HOW TO PLAY?', 30)
            label.rect.left = 190
            label.rect.top = 25
            self.objects.append(label)

            label = LabelObject('Move your ship by pressing up and down.', 18)
            label.rect.left = 120
            label.rect.top = 120
            self.objects.append(label)

            label = LabelObject('To shoot press spacebar.', 18)
            label.rect.left = 120
            label.rect.top = 145
            self.objects.append(label)

            image = ImageObject('ship.png')
            image.rect.left = 45
            image.rect.top = 120
            self.objects.append(image)

            image = ImageObject('arrows.png')
            image.rect.left = 49
            image.rect.top = 176
            self.objects.append(image)

            image = ImageObject('arrows.png')
            image.rect.left = 49
            image.rect.top = 75
            image.surface_to_draw = pygame.transform.flip(image.surface_to_draw, False, True)
            self.objects.append(image)

            label = LabelObject('But watch out for', 18)
            label.rect.left = 120
            label.rect.top = 240
            self.objects.append(label)

            label = LabelObject('THE BOSS!', 28)
            label.rect.left = 350
            label.rect.top = 235
            self.objects.append(label)

            label = LabelObject('You must kill him before he shows', 18)
            label.rect.left = 200
            label.rect.top = 340
            self.objects.append(label)

            label = LabelObject('9 TIMES', 68)
            label.rect.left = 240
            label.rect.top = 370
            self.objects.append(label)

            image = ImageObject('boss.png')
            image.rect.left = 39
            image.rect.top = 300
            self.objects.append(image)

            self.objects.append(image)

        for element in self.objects:
            element.draw_on_surface(surface)

        buffer = pygame.image.tostring(surface, 'RGB')
        self.buffer = buffer
        self.buffer_size = surface.get_size()

    def process_inputs(self, events):
        for event in events:
            if event.type == KEYDOWN:
                self.switch_board = True

    def is_time_to_switch_board(self):
        return self.switch_board

    def get_next_board(self):
        return SwitchBoard(self.buffer, self.buffer_size, GameBoard())
