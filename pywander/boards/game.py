import os
import pygame
from pygame.locals import K_DOWN, K_UP, K_SPACE
from pywander.boards.base import BoardBase
from pywander.objects.image import ImageObject
from pywander.sprites.ship import ShipSprite
from pywander.sprites.enemy import EnemySprite
from pywander.sprites.boss import BossSprite
from pywander.sprites.asteroid import AsteroidSprite
from pywander.sprites.bullet import BulletSprite


PLAYER_WON = 1
PLAYER_LOSE = 2

class GameBoard(BoardBase):
    status = None
    ship_speed = 0.39
    ship_top = 0.00
    bullets = []
    last_fire_time = 0
    fire_delay = 500

    background = None
    ship = None
    bullets_group = None
    enemy_group = None
    inactive_group = None
    
    level = 1
    level_file = None
    last_file_read = 0
    level_speed = 1000

    def __init__(self, level=1):
        self.level = level

        self.background = ImageObject('background.png')

        self.ship = ShipSprite()
        self.bullets_group = pygame.sprite.Group()
        self.enemy_group = pygame.sprite.Group()
        self.inactive_group = pygame.sprite.Group()

        self.level_file = open(os.path.join('data', 'level.txt'))
        self.level_file.readline()  # First line indicates just limit of file width

    def process_draw_on_surface(self, surface):
        # TODO: Performance issues here...
        # self.background.draw_on_surface(surface)

        for bullet in self.bullets_group.sprites():
            bullet.image.rect.left += 1
            if bullet.image.rect.left >= 640:
                self.bullets_group.remove(bullet)
            else:
                bullet.draw_on_surface(surface)

        self.ship.image.rect.top = int(self.ship_top)
        self.ship.draw_on_surface(surface)

        for enemy in self.enemy_group.sprites():
            enemy.draw_on_surface(surface)
        
        for inactive in self.inactive_group.sprites():
            inactive.draw_on_surface(surface)
            if inactive.is_completed():
                self.inactive_group.remove(inactive)

        for hit in pygame.sprite.groupcollide(self.enemy_group, self.bullets_group, 1, 1):
            if isinstance(hit, BossSprite):
                self.status = PLAYER_WON
                return False
            
            if isinstance(hit, EnemySprite):
                hit.show_explosion()
                self.inactive_group.add(hit)

        if pygame.sprite.spritecollideany(self.ship, self.enemy_group):
            self.status = PLAYER_LOSE
        else:
            self.read_level_info()

    def process_inputs(self, events):
        key = pygame.key.get_pressed()
        if key[K_DOWN]:
            self.move_ship_down()
        if key[K_UP]:
            self.move_ship_up()
        if key[K_SPACE]:
            self.fire_bullet()

    def is_time_to_switch_board(self):
        return self.status is not None

    def get_next_board(self):
        from pywander.boards.won import WonBoard
        from pywander.boards.lose import LoseBoard

        if self.status == PLAYER_WON:
            return WonBoard(self.level + 1)
        else:
            return LoseBoard()

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
            bullet.image.rect.left = self.ship.image.rect.width / 2
            bullet.image.rect.top = self.ship.image.rect.top + (self.ship.image.rect.height / 2 - 9)
            self.bullets_group.add(bullet)
            self.last_fire_time = time_now

    def add_enemy(self, key):
        enemy = EnemySprite()
        enemy.image.rect.left = 680
        enemy.image.rect.top = key * 30
        self.enemy_group.add(enemy)

    def add_asteroid(self, key):
        enemy = AsteroidSprite()
        enemy.image.rect.left = 680
        enemy.image.rect.top = key * 30
        self.enemy_group.add(enemy)

    def add_boss(self, key):
        enemy = BossSprite()
        enemy.image.rect.left = 420
        enemy.image.rect.top = key * 30
        self.enemy_group.add(enemy)

    def read_level_info(self):
        time_now = pygame.time.get_ticks()
        if self.last_file_read + self.level_speed < time_now:
            line = self.level_file.readline()
            key = 0
            for obj in line:
                if obj == '^':
                    self.add_enemy(key)
                if obj == 'O':
                    self.add_asteroid(key)
                if obj == '@':
                    self.add_boss(key)
                key += 1
            self.last_file_read = time_now
