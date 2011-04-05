from pygame.locals import KEYDOWN
from pywander.boards.base import BoardBase
from pywander.boards.game import GameBoard
from pywander.boards.game_completed import GameCompletedBoard
from pywander.objects.label import LabelObject


class WonBoard(BoardBase):
    switch_board = False
    labels = []
    level = None

    def __init__(self, level):
        self.level = level

    def process_draw_on_surface(self, surface):
        if self.level < 10:
            if self.labels == []:
                label = LabelObject('CONGRATS', 81, (160, 160, 160))
                label.rect.left = 61
                label.rect.top = 114
                self.labels.append(label)
    
                level_finished = self.level - 1
                label = LabelObject('YOU HAVE JUST FINISHED LEVEL %d,' % level_finished, 27, (160, 160, 160))
                label.rect.left = 61
                label.rect.top = 204
                self.labels.append(label)

                label = LabelObject('PREPARE FOR NEXT LEVEL!', 27, (160, 160, 160))
                label.rect.left = 61
                label.rect.top = 244
                self.labels.append(label)

            for label in self.labels:
                label.draw_on_surface(surface)
        else:
            if self.labels == []:
                label = LabelObject('COMPLETED', 81, (160, 160, 160))
                label.rect.left = 41
                label.rect.top = 114
                self.labels.append(label)
    
                label = LabelObject('YOU HAVE JUST FINISHED LAST', 27, (160, 160, 160))
                label.rect.left = 41
                label.rect.top = 204
                self.labels.append(label)

                label = LabelObject('LEVEL, CONGRATS!', 27, (160, 160, 160))
                label.rect.left = 41
                label.rect.top = 244
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
        if self.level < 10:
            return GameBoard(self.level)
        else:
            return GameCompletedBoard()
