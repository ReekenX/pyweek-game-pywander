import pygame
from pywander.boards.base import BoardBase
from pywander.objects.image import ImageObject


class SwitchBoard(BoardBase):
    switch_board = False
    next_board = None
    image = None
    is_completed = False
    transparency = 0.0
    transparency_speed = 6.54
    go_to_dark = True

    def __init__(self, buffer, buffer_size, board_after):
        self.image = pygame.image.frombuffer(buffer, buffer_size, 'RGB')
        self.next_board = board_after
        self.background = ImageObject('background.png')

    def process_draw_on_surface(self, surface):
        if self.go_to_dark:
            surface.blit(self.image, (0, 0))

            if self.transparency < 255 - self.transparency_speed:
                self.transparency += self.transparency_speed
            else:
                self.go_to_dark = False
            transparency_rgb_with_alpha = (160,
                                           160,
                                           160,
                                           self.transparency)
            transparency = pygame.surface.Surface((640, 480)).convert_alpha()
            transparency.fill(transparency_rgb_with_alpha)
            surface.blit(transparency, (0, 0))
        else:
            self.background.draw_on_surface(surface)

            if self.transparency > 0 + self.transparency_speed:
                self.transparency -= self.transparency_speed
            else:
                self.switch_board = True
            transparency_rgb_with_alpha = (160,
                                           160,
                                           160,
                                           self.transparency)
            transparency = pygame.surface.Surface((640, 480)).convert_alpha()
            transparency.fill(transparency_rgb_with_alpha)
            surface.blit(transparency, (0, 0))

    def process_inputs(self, events):
        pass

    def is_time_to_switch_board(self):
        return self.switch_board

    def get_next_board(self):
        return self.next_board
