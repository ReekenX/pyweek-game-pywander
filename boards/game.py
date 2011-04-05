from pygame.locals import KEYDOWN
from boards.base import BoardBase
from boards.won import WonBoard
from objects.label import LabelObject


class GameBoard(BoardBase):
    switch_board = False

    def __init__(self):
        self.label = LabelObject('Board of game...')

    def process_draw_on_surface(self, surface):
        self.label.draw_on_surface(surface)

    def process_inputs(self, events):
        for event in events:
            if event.type == KEYDOWN:
                self.switch_board = True

    def is_time_to_switch_board(self):
        return self.switch_board

    def get_next_board(self):
        return WonBoard()
