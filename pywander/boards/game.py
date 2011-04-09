import os
import pygame
from pygame.locals import K_DOWN, K_UP, K_LEFT, K_RIGHT, K_SPACE
from pywander.boards.base import BoardBase
from pywander.objects.image import ImageObject
from pywander.objects.label import LabelObject
from pywander.objects.sound import SoundObject
from pywander.sprites.ship import ShipSprite
from pywander.sprites.enemy import EnemySprite
from pywander.sprites.boss import BossSprite
from pywander.sprites.asteroid import AsteroidSprite
from pywander.sprites.bullet import BulletSprite


PLAYER_WON = 1
PLAYER_LOSE = 2

class GameBoard(BoardBase):
    status = None
    score = 0
    life = 100
    boss_life = 100

    bullets = []

    background = None
    background_x = 0
    background_speed = 0.07
    background_time = 0
    background_width = 3161

    ship = None
    bullets_group = None
    enemy_group = None
    inactive_group = None

    level = 1
    level_file = None
    last_file_read = 0
    level_speed = 1000

    attempts_left = 9

    def __init__(self, level=1):
        self.level = level

        self.background = ImageObject('background.png')

        self.ship = ShipSprite()
        self.bullets_group = pygame.sprite.Group()
        self.enemy_group = pygame.sprite.Group()
        self.inactive_group = pygame.sprite.Group()

        self.level_file = open(os.path.join('data', 'levels', 'level_%d.txt' % self.level))
        self.level_file.readline()  # First line indicates just limit of file width

    def process_draw_on_surface(self, surface):
        time_before = self.background_time
        if self.background_time != 0:
            self.background_time = pygame.time.get_ticks()
            elapsed = self.background_time - time_before
        else:
            self.background_time = pygame.time.get_ticks()
            elapsed = 0
        self.background_x -= int(elapsed * self.background_speed)
        if self.background_x < -self.background_width:
            self.background_x += self.background_width
        for i in range(3):
            self.background.rect.left = int(self.background_x) + (self.background_width * (i - 1))
            self.background.draw_on_surface(surface, self)

        score_label = LabelObject('Score: %d' % self.score, 14)
        score_label.change_realign('top-right', right=15, top=15)
        score_label.draw_on_surface(surface, self)

        life_label = LabelObject('Life: %d' % self.life, 14)
        life_label.change_realign('top-left', left=15, top=15)
        life_label.draw_on_surface(surface, self)

        life_label = LabelObject('Attempts left: %d' % self.attempts_left, 14)
        life_label.change_realign('top-center', top=15)
        life_label.draw_on_surface(surface, self)

        for bullet in self.bullets_group.sprites():
            if bullet.image.rect.left >= 640:
                self.bullets_group.remove(bullet)
            else:
                bullet.draw_on_surface(surface, self)

        self.ship.draw_on_surface(surface, self)

        for enemy in self.enemy_group.sprites():
            if isinstance(enemy, EnemySprite):
                if enemy.is_completed():
                    self.enemy_group.remove(enemy)
            enemy.draw_on_surface(surface, self)

        for inactive in self.inactive_group.sprites():
            if isinstance(inactive, EnemySprite):
                if inactive.is_completed():
                    self.inactive_group.remove(inactive)
                    continue
            inactive.draw_on_surface(surface, self)

        for hit in pygame.sprite.groupcollide(self.enemy_group, self.bullets_group, 0, 1):
            if isinstance(hit, AsteroidSprite):
                self.score += 9

            if isinstance(hit, BulletSprite):
                hit.kill()

            if isinstance(hit, BossSprite):
                self.score += 13
                hit.hit()
                self.boss_life = hit.life
                if hit.life <= 0:
                    self.status = PLAYER_WON
                    return False

            if isinstance(hit, EnemySprite):
                self.score += 7
                hit.kill()
                hit.show_explosion()
                sound = SoundObject()
                sound.play('boom', 0)
                self.inactive_group.add(hit)

        hit = pygame.sprite.spritecollideany(self.ship, self.enemy_group)
        if hit:
            fatal = isinstance(hit, AsteroidSprite) or isinstance(hit, BossSprite)
            if not fatal:
                hit.kill()

                if isinstance(hit, EnemySprite):
                    hit.show_explosion()
                    sound = SoundObject()
                    sound.play('boom', 0)

                self.life -= 25
            else:
                self.status = PLAYER_LOSE
        else:
            self.read_level_info()

        if self.attempts_left == 0 or self.life == 0:
            self.status = PLAYER_LOSE

        buffer = pygame.image.tostring(surface, 'RGB')
        self.buffer = buffer
        self.buffer_size = surface.get_size()

    def process_inputs(self, events):
        key = pygame.key.get_pressed()
        if key[K_DOWN]:
            self.ship.move_ship_down()
        if key[K_UP]:
            self.ship.move_ship_up()
        if key[K_SPACE]:
            self.ship.fire_bullet(self.bullets_group)
        if key[K_LEFT]:
            self.ship.move_ship_left()
        if key[K_RIGHT]:
            self.ship.move_ship_right()

    def is_time_to_switch_board(self):
        return self.status is not None

    def get_next_board(self):
        from pywander.boards.switch import SwitchBoard
        from pywander.boards.won import WonBoard
        from pywander.boards.lose import LoseBoard

        if self.status == PLAYER_WON:
            return SwitchBoard(self.buffer, self.buffer_size, WonBoard(self.level + 1))
        else:
            return SwitchBoard(self.buffer, self.buffer_size, LoseBoard())

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
        enemy.life = self.boss_life
        enemy.image.rect.left = 645
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
