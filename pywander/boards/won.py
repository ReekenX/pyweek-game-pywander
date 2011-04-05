from pygame.locals import KEYDOWN
from pywander.boards.base import BoardBase
from pywander.boards.game import GameBoard
from pywander.objects.label import LabelObject


class WonBoard(BoardBase):
    switch_board = False

    def __init__(self, level):
        self.label = LabelObject('You won! Going to level %d.' % level)
        self.level = level

    def process_draw_on_surface(self, surface):
        self.label.draw_on_surface(surface)

    def process_inputs(self, events):
        for event in events:
            if event.type == KEYDOWN:
                self.switch_board = True

    def is_time_to_switch_board(self):
        return self.switch_board

    def get_next_board(self):
        return GameBoard(self.level)
