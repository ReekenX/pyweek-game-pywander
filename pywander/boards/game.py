import pygame
from pygame.locals import KEYDOWN, K_RETURN, K_DOWN, K_UP, K_SPACE
from pywander.boards.base import BoardBase
from pywander.boards.won import WonBoard
from pywander.objects.label import LabelObject
from pywander.sprites.ship import ShipSprite
from pywander.sprites.bullet import BulletSprite


class GameBoard(BoardBase):
    ship_speed = 0.39
    ship_top = 0.00
    switch_board = False
    bullets = []
    last_fire_time = 0
    fire_delay = 500

    def __init__(self):
        self.label = LabelObject('Board of game...')
        self.ship = ShipSprite()

    def process_draw_on_surface(self, surface):
        self.label.draw_on_surface(surface)

        for bullet in self.bullets:
            bullet.move_and_draw(surface)
            if bullet.image.rect.left >= 640:
                self.bullets.remove(bullet)

        self.ship.image.rect.top = int(self.ship_top)
        self.ship.image.draw_on_surface(surface)

        #tmp = LabelObject('Speed: ' + str(self.ship_speed))
        #tmp.rect.left = 580
        #tmp.draw_on_surface(surface)

    def process_inputs(self, events):
        for event in events:
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    self.switch_board = True

        key = pygame.key.get_pressed()
        if key[K_DOWN]:
            self.move_ship_down()
        if key[K_UP]:
            self.move_ship_up()
        if key[K_SPACE]:
            self.fire_bullet()

    def is_time_to_switch_board(self):
        return self.switch_board

    def get_next_board(self):
        return WonBoard()

    def move_ship_down(self):
        if self.ship.image.rect.top + self.ship_speed < 380:
            self.ship_top += self.ship_speed

    def move_ship_up(self):
        if self.ship.image.rect.top - self.ship_speed > 0:
            self.ship_top -= self.ship_speed

    def fire_bullet(self):
        time_now = pygame.time.get_ticks()
        if self.last_fire_time + self.fire_delay < time_now:
            bullet = BulletSprite()
            bullet.image.rect.left = 50
            bullet.image.rect.top = self.ship.image.rect.top + 45
            self.bullets.append(bullet)
            self.last_fire_time = time_now
