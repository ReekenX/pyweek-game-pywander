from pygame.locals import KEYDOWN
from pywander.boards.base import BoardBase
from pywander.objects.label import LabelObject


class LoseBoard(BoardBase):
    switch_board = False

    def __init__(self):
        self.label = LabelObject('Board to show that you lose...')

    def process_draw_on_surface(self, surface):
        self.label.draw_on_surface(surface)

    def process_inputs(self, events):
        for event in events:
            if event.type == KEYDOWN:
                self.switch_board = True

    def is_time_to_switch_board(self):
        return self.switch_board

    def get_next_board(self):
        return None
