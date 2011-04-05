from pygame.locals import KEYDOWN
from pywander.boards.base import BoardBase
from pywander.objects.label import LabelObject


class LoseBoard(BoardBase):
    switch_board = False
    labels = []

    def process_draw_on_surface(self, surface):
        if self.labels == []:
            label = LabelObject('SORRY', 121, (160, 160, 160))
            label.rect.left = 71
            label.rect.top = 104
            self.labels.append(label)

            label = LabelObject('BUT YOU LOSE. JUST DON''T CRY,', 27, (160, 160, 160))
            label.rect.left = 71
            label.rect.top = 224
            self.labels.append(label)

            label = LabelObject('YOU CAN PLAY AGAIN! :)', 27, (160, 160, 160))
            label.rect.left = 71
            label.rect.top = 264
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
