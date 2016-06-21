import pygame
from pygame.locals import *

class Indicator:

    def __init__(self, screen=None, x=0, y=0, icons = [], icon_size=None):
        if screen:
            start_state_icon = icons[0];
            if icon_size:
                start_state_icon = pygame.transform.scale(start_state_icon, icon_size)
            screen.blit(start_state_icon, (x, y))


    def change_state(self, state_num):
        state_icon = icons[screen_num]
        if self.icon_size:
            state_icon = pygame.transform.scale(state_icon, self.icon_size)
        screen.blit(state_icon, (self.x, self.y))
