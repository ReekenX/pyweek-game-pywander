import pygame


class ObjectBase(object):
    last_realign = None
    realign = None
    realign_params = None
    surface_to_draw = None  # Should be initialized in __init__
    rect = None

    def __init__(self, *args, **kwargs):
        # I don't know why exactly Python dislikes these to be in variables
        # list above, so initializing these here...
        self.transparency = {
            'transparency_start': 0,
            'transparency_end': 0,
            'time_start': 0,
            'time_end': 0,
            'is_animating': False
        }
        self.movement = {
            'movement_start': [0, 0],
            'movement_end': [0, 0],
            'time_start': 0,
            'time_end': 0,
            'is_animating': False
        }
        orig_rect = self.get_orig_surface_rect()
        self.rect = pygame.Rect(orig_rect.left, orig_rect.top,
                               orig_rect.width, orig_rect.height)

    def is_animating_transparency(self):
        return self.transparency['is_animating']

    def stop_animating_transparency(self):
        self.transparency['is_animating'] = False

    def animate_transparency(self, transparency_to, time):
        self.transparency['time_start'] = pygame.time.get_ticks()
        self.transparency['time_end'] = self.transparency['time_start'] + time
        self.transparency['transparency_end'] = transparency_to
        self.transparency['is_animating'] = True

    def get_rect(self):
        return self.rect

    def get_orig_surface_rect(self):
        return self.surface_to_draw.get_rect()

    def get_transparency_value(self):
        if not self.transparency['is_animating']:
            return self.transparency['transparency_start']

        time_now = pygame.time.get_ticks()
        if self.transparency['is_animating'] and time_now >= self.transparency['time_end']:
            self.stop_animating_transparency()
            self.transparency['transparency_start'] = self.transparency['transparency_end']
            return self.transparency['transparency_end']

        time_elapsed = time_now - self.transparency['time_start']
        time_to_elapse = self.transparency['time_end'] - self.transparency['time_start']
        time_elapsed_percently = time_elapsed * 100 / time_to_elapse
        if time_elapsed_percently == 0:
            time_elapsed_percently = 1

        transparency_to_elapse = self.transparency['transparency_end'] - self.transparency['transparency_start']
        transparency_now = abs(transparency_to_elapse) * time_elapsed_percently / 100
        if transparency_to_elapse < 0:
            transparency_now = self.transparency['transparency_start'] - transparency_now
        return transparency_now

    def is_animating_movement(self):
        return self.movement['is_animating']

    def stop_animating_movement(self):
        self.movement['is_animating'] = False

    def animate_movement(self, movement_to, time):
        self.movement['time_start'] = pygame.time.get_ticks()
        self.movement['time_end'] = self.movement['time_start'] + time
        self.movement['movement_end'] = movement_to
        self.movement['is_animating'] = True

    def recount_movement_coords(self):
        if not self.movement['is_animating']:
            return False

        time_now = pygame.time.get_ticks()
        if self.movement['is_animating'] and time_now >= self.movement['time_end']:
            self.stop_animating_movement()
            self.rect.left = self.movement['movement_end'][0]
            self.rect.top = self.movement['movement_end'][1]
            return False

        time_elapsed = time_now - self.movement['time_start']
        time_to_elapse = self.movement['time_end'] - self.movement['time_start']
        time_elapsed_percently = time_elapsed * 100 / time_to_elapse
        if time_elapsed_percently == 0:
            time_elapsed_percently = 1

        total_x_to_elapse = self.movement['movement_end'][0] - self.rect.left
        total_y_to_elapse = self.movement['movement_end'][1] - self.rect.top

        x_elapsed = total_x_to_elapse * time_elapsed_percently / 100
        y_elapsed = total_y_to_elapse * time_elapsed_percently / 100

        self.rect.left += x_elapsed
        self.rect.top += y_elapsed

    def draw_on_surface(self, surface, rect=None):
        if self.is_realign_changed():
            self.realign_on_surface(surface)

        self.recount_movement_coords()
        surface.blit(self.surface_to_draw, self.get_rect())

        try:
            transparency_color = surface.get_at((self.rect.left, self.rect.top))
            transparency_rgb_with_alpha = (transparency_color.r,
                                           transparency_color.g,
                                           transparency_color.b,
                                           self.get_transparency_value())
            transparency = pygame.surface.Surface((self.rect.width, self.rect.height)).convert_alpha()
            transparency.fill(transparency_rgb_with_alpha)
            surface.blit(transparency, self.rect)
        except:
            pass

    def is_realign_changed(self):
        return self.realign != self.last_realign

    def change_realign(self, realign, **kwargs):
        self.last_realign = self.realign
        self.realign = realign
        self.realign_params = kwargs

    def realign_on_surface(self, surface):
        if self.realign == 'center-center':
            self.rect.center = (surface.get_rect().width / 2,
                                surface.get_rect().height / 2)
            self.change_realign(self.realign)
        elif self.realign == 'bottom-right':
            self.rect.midright = (surface.get_rect().width - self.realign_params['right'],
                                  surface.get_rect().height - self.realign_params['bottom'])
        elif self.realign == 'top-right':
            self.rect.right = surface.get_rect().width - self.realign_params['right']
            self.rect.top = self.realign_params['top']

        elif self.realign == 'top-left':
            self.rect.left = self.realign_params['left']
            self.rect.top = self.realign_params['top']
