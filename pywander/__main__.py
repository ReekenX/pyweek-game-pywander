import os
import sys
import pygame
from pywander.boards.startup import StartupBoard
from pywander.objects.label import LabelObject
from pywander.objects.sound import SoundObject


def main():
    os.environ['SDL_VIDEO_WINDOW_POS'] = '400,200'
    SCREEN_WIDTH = 640
    SCREEN_HEIGHT = 480
    SCREEN_BACKGROUND = 232, 232, 232

    pygame.init()
    surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT),
                                  pygame.DOUBLEBUF)
    pygame.display.set_caption('Pywander - save the world in less than 9 times')

    clock = pygame.time.Clock()
    board = StartupBoard()
    sound = SoundObject()
    sound.play('background', -1)

    while board is not None:
        surface.fill(SCREEN_BACKGROUND)

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.locals.KEYDOWN and \
               event.key == pygame.locals.K_ESCAPE:
                sys.exit(0)

        board = board.update(surface, events)

        fps = clock.get_fps()
        fps_label = LabelObject('FPS: %d' % fps, 14)
        fps_label.change_realign('bottom-left', left=15, bottom=25)
        fps_label.draw_on_surface(surface)

        pygame.display.flip()
        clock.tick(200)
