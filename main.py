import pygame
from pygame.locals import *
import guard_station
import prison_cell
import time

class PrisonSim:
    def __init__(self):
        self._running = True
        self.screen = None
        self.size = self.width, self.height = 1200, 700

    def on_init(self):
        #Initialize screen
        pygame.init()
        self.font = pygame.font.SysFont('Times', 25)
        pygame.display.set_caption('Ybox Simulation')
        self.screen = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self.screen.fill((black))

        self.function_map = self.create_function_map()

        #TODO update
        self.ybox = None#ybox.YBox()
        self.ybox_map = {}

        x_padding = 50
        y_padding = 50

        cell_panel_width = 325
        cell_panel_heigh = 300

        #create the guard station panel with number of cells
        self.guard_station_panel = guard_station.GuardStation(self, 3, 50, 450)

        #create each cell at given location
        cell_one_panel = prison_cell.PrisonCell(self, 1, x_padding, y_padding)
        cell_two_panel = prison_cell.PrisonCell(self, 2, 2*x_padding+cell_panel_width, y_padding)
        cell_three_panel = prison_cell.PrisonCell(self, 3, 3*x_padding+2*cell_panel_width, y_padding)

        #add all cells to list
        self.cell_door_panels = [cell_one_panel, cell_two_panel, cell_three_panel]

        pygame.display.update()
        self._running = True

    #this function is used to map inputs to functions. Inputs are placeholders.
    def create_function_map(self):
        return {'CELL ONE UNLOCK': lambda x: x.unlock_cell(1),
                'CELL TWO UNLOCK': lambda x: x.unlock_cell(2),
                'CELL THREE UNLOCK': lambda x: x.unlock_cell(3),
                'CELL ONE SECURE':  lambda x: x.show_secure(1),
                'CELL TWO SECURE': lambda x: x.show_secure(2),
                'CELL THREE SECURE': lambda x: x.show_secure(3)
        }



    #Handle all events
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        else: #Determine if button was clicked
            for i, cell_btn in enumerate(self.guard_station_panel.cell_btns):
                if 'click' in cell_btn.handleEvent(event):
                    self.guard_panel_click_handler(i)

            for cell in self.cell_door_panels:
                if 'click' in cell.key_btn.handleEvent(event):
                    self.cell_unlock_click_handler(cell)

            pygame.display.update()

    #WRITE TO PLC INPUT OPEN
    def guard_panel_click_handler(self, cell_num):
        #TODO replace code with write to PLC
        self.cell_door_panels[cell_num].cell_door.change_state()
        self.cell_door_panels[cell_num].cell_door_indicator.change_state()
        self.cell_door_panels[cell_num].lock_indicator.change_state()
        ###

    def cell_unlock_click_handler(self, cell):
        #TODO replace code
        cell.cell_door.change_state()
        cell.cell_door_indicator.change_state()
        cell.lock_indicator.change_state()
        ###

    #Recieved unlock command from PLC
    def unlock_cell(self, cell):
        self.cell_door_panels[cell_num].cell_door.change_state(1)
        self.cell_door_panels[cell_num].lock_indicator.change_state(1)

    #Recieved secured indicator command from PLC
    def show_secure(self, cell):
        self.cell_door_panels[cell_num].cell_door_indicator.change_state(0)

    def read_ybox(self):
        new_input_map = {} #self.ybox.getMap()
        self.compare_maps(new_input_map)


    def compare_maps(self, new_input_map):
        old_input_map = self.ybox_map
        for key,value in new_input_map.items():
            if old_input_map.get(key) != value:
                #call correct function
                pass


    def on_loop(self):
        self.read_ybox()

    def on_render(self):
        pass
    def on_cleanup(self):
        pygame.quit()

    #start program
    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while( self._running ):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()

if __name__ == "__main__" :

    green = (200,0,0)
    white = (255, 255, 255)
    black = (0,0,0)
    grey = (200, 200, 200)
    dark_grey = (140, 140, 140)
    light_blue = (0, 0, 255)
    dark_blue = (0, 0, 150)

    prisonSim = PrisonSim()
    prisonSim.on_execute()
