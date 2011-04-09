import os
import pygame


class SoundObject(object):
    def play(self, name, loops):
        sound_file_name = os.path.join('data', 'sounds', name + '.wav')
        sound = pygame.mixer.Sound(sound_file_name)
        sound.play(loops)
        return sound
