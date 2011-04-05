# coding=utf8
from pygame.locals import KEYDOWN
from pywander.boards.base import BoardBase
from pywander.objects.label import LabelObject


class GameCompletedBoard(BoardBase):
    switch_board = False
    labels = []

    def process_draw_on_surface(self, surface):
        if self.labels == []:
            label = LabelObject('THE END', 81, (160, 160, 160))
            label.rect.left = 51
            label.rect.top = 114
            self.labels.append(label)

            label = LabelObject('This game was developed for Pyweek', 23, (160, 160, 160))
            label.rect.left = 51
            label.rect.top = 204
            self.labels.append(label)

            label = LabelObject('challenge 12. Released under GPL.', 23, (160, 160, 160))
            label.rect.left = 51
            label.rect.top = 244
            self.labels.append(label)

            label = LabelObject('AUTHOR: REMIGIJUS JARMALAVICIUS', 23, (160, 160, 160))
            label.rect.left = 51
            label.rect.top = 344
            self.labels.append(label)

        for label in self.labels:
            label.draw_on_surface(surface)

    def process_inputs(self, events):
        for event in events:
            if event.type == KEYDOWN:
                self.switch_board = True

    def is_time_to_switch_board(self):
        return self.switch_board

    def get_next_board(self):
        return None
