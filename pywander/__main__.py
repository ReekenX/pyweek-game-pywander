import os
import sys
import pygame
from pywander.boards.startup import StartupBoard


def main():
    os.environ['SDL_VIDEO_WINDOW_POS'] = '400,200'
    SCREEN_WIDTH = 640
    SCREEN_HEIGHT = 480
    SCREEN_BACKGROUND = 232, 232, 232

    pygame.init()
    surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT),
                                  pygame.DOUBLEBUF)
    pygame.display.set_caption('Pywander - Finish level 9 times')

    clock = pygame.time.Clock()
    board = StartupBoard()

    while board is not None:
        clock.tick(5000)
        surface.fill(SCREEN_BACKGROUND)

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.locals.KEYDOWN and \
               event.key == pygame.locals.K_ESCAPE:
                sys.exit(0)

        board = board.update(surface, events)
        pygame.display.flip()
