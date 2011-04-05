from pygame.locals import KEYDOWN, K_RETURN, K_DOWN, K_UP
from pywander.boards.base import BoardBase
from pywander.boards.won import WonBoard
from pywander.objects.label import LabelObject
from pywander.objects.image import ImageObject


class GameBoard(BoardBase):
    ship_speed = 5
    switch_board = False

    def __init__(self):
        self.label = LabelObject('Board of game...')
        self.ship = ImageObject('ship.png')

    def process_draw_on_surface(self, surface):
        self.label.draw_on_surface(surface)
        self.ship.draw_on_surface(surface)

    def process_inputs(self, events):
        for event in events:
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    self.switch_board = True
                if event.key == K_DOWN:
                    self.move_ship_down()
                if event.key == K_UP:
                    self.move_ship_up()

    def is_time_to_switch_board(self):
        return self.switch_board

    def get_next_board(self):
        return WonBoard()

    def move_ship_down(self):
        if self.ship.rect.top + self.ship_speed < 380:
            self.ship.rect.top += self.ship_speed

    def move_ship_up(self):
        if self.ship.rect.top - self.ship_speed > 0:
            self.ship.rect.top -= self.ship_speed
