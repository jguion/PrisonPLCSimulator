import pygame
from pygame.locals import *

class Indicator:

    def __init__(self, sim=None, x=0, y=0, icons = [], icon_size=None):
        if sim:
            self.state_num = 0
            self.x = x
            self.y = y
            self.icons = icons
            self.sim = sim
            self.icon_size = icon_size
            start_state_icon = icons[0]

            if icon_size:
                start_state_icon = pygame.transform.scale(start_state_icon, icon_size)
            sim.screen.blit(start_state_icon, (x, y))


    def change_state(self, screen=None, state_num=None):
        if state_num is None:
            self.state_num = (self.state_num + 1) % 2
        print ("state num %s" %self.state_num)
        print(self.icons)
        state_icon = self.icons[self.state_num]
        if self.icon_size:
            state_icon = pygame.transform.scale(state_icon, self.icon_size)
        if screen is None:
            screen = self.sim.screen
        screen.blit(state_icon, (self.x, self.y))
