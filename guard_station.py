import pygame
from pygame.locals import *

import pygbutton

class GuardStation:

    def __init__(self, sim=None, num_cells=0, x=0, y=0):
        if sim:
            screen = sim.screen
            font = sim.font
            self.cell_btns = []
            btn_height = 40;
            btn_width = 100;
            cell_padding_x = 25
            cell_padding_y = 25
            grey = (200, 200, 200)
            dark_grey = (140, 140, 140)
            white = (255, 255, 255)
            black = (0,0,0)

            title_height = 25
            panel_width = btn_width * num_cells + (num_cells+1)*cell_padding_x
            panel_height = btn_height + 2*cell_padding_y + title_height

            guard_display_panel = pygame.draw.rect(screen, (grey), (x, y, panel_width, panel_height))

            #Title
            screen.blit(font.render('Guard Station Panel', True, (black)), (x+20, y+10))

            cell_start_x = x + cell_padding_x
            cell_start_y = y + cell_padding_y+title_height

            for i in range(0, num_cells):
                cell_num = i+1
                button_text = "Cell %s" % cell_num

                cell_btn = pygbutton.PygButton((cell_start_x, cell_start_y, btn_width, btn_height), button_text)
                cell_btn.draw(screen)

                self.cell_btns.append(cell_btn)

                cell_start_x += btn_width + cell_padding_x
