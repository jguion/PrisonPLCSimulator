import pygame
from pygame.locals import *

import pygbutton
import indicator

class PrisonCell:

    def __init__(self, sim=None, cell_num=0, x=0, y=0, current_state=0):
        if sim is not None:
            cell_padding_x = 25
            cell_padding_y = 25
            title_height = 25
            indicators_panel_width = 100
            grey = (200, 200, 200)
            dark_grey = (140, 140, 140)
            white = (255, 255, 255)
            black = (0,0,0)
            screen = sim.screen
            font = sim.font

            panel_width = 3*cell_padding_x+100+150
            panel_height = 2*cell_padding_y+250+title_height

            cell_door_start_x = x+2*cell_padding_x+indicators_panel_width
            cell_door_start_y = y+cell_padding_y+title_height

            cell_control_panel = pygame.draw.rect(screen, (grey), (x, y, panel_width, panel_height))

            #Title
            screen.blit(font.render('Cell %s' % cell_num, True, (black)), (x+10, y+10))

            #Cell Door
            cell_door_dimensions = ((150,250))
            closed_door_icon = pygame.image.load ("images/closedDoor.png")
            open_door_icon= pygame.image.load ("images/openDoor.png")
            cell_door_icons = [closed_door_icon, open_door_icon]
            self.cell_door = indicator.Indicator(sim, cell_door_start_x, cell_door_start_y, cell_door_icons, cell_door_dimensions)

            #Control Panel
            green_icon = pygame.image.load("images/greenLightAlt.png")
            red_icon = pygame.image.load("images/redLightAlt.png")

            indicator_start_x = x+cell_padding_x
            indicator_start_y = cell_door_start_y
            indicator_icons = [green_icon, red_icon]
            indicator_dimensions = ((75,75))
            self.cell_door_indicator = indicator.Indicator(sim, indicator_start_x, indicator_start_y, indicator_icons, indicator_dimensions)

            key_start_x = indicator_start_x
            key_start_y = indicator_start_y+150
            key_btn_width = 90
            key_btn_height = 40
            key_btn_text = "Unlock Key"

            self.key_btn = pygbutton.PygButton((key_start_x, key_start_y, key_btn_width, key_btn_height), key_btn_text)
            self.key_btn.draw(screen)
