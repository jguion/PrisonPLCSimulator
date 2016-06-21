import pygame
from pygame.locals import *
import guard_station
import prison_cell

class PrisonSim:
    def __init__(self):
        self._running = True
        self.screen = None
        self.size = self.width, self.height = 1025, 700

    def on_init(self):
        #Initialize screen
        pygame.init()
        self.font = pygame.font.SysFont('Times', 25)
        pygame.display.set_caption('Ybox Simulation')
        self.screen = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self.screen.fill((black))

        x_padding = 50
        y_padding = 50

        cell_panel_width = 325
        cell_panel_heigh = 300

        #create the guard station panel with number of cells
        self.guard_station_panel = guard_station.GuardStation(self, 2, 50, 450)

        #create each cell at given location
        cell_one_panel = prison_cell.PrisonCell(self, 1, x_padding, y_padding)
        cell_two_panel = prison_cell.PrisonCell(self, 2, 2*x_padding+cell_panel_width, y_padding)

        #add all cells to list
        self.cell_door_panels = [cell_one_panel, cell_two_panel]

        pygame.display.update()
        self._running = True

    #Handle all events
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        else: #Determine if button was clicked
            for i, cell_btn in enumerate(self.guard_station_panel.cell_btns):
                if 'click' in cell_btn.handleEvent(event):
                    self.cell_door_panels[i].cell_door.change_state()
                    self.cell_door_panels[i].cell_door_indicator.change_state()
                    self.cell_door_panels[i].lock_indicator.change_state()
            for cell in self.cell_door_panels:
                if 'click' in cell.key_btn.handleEvent(event):
                    cell.cell_door.change_state()
                    cell.cell_door_indicator.change_state()
                    cell.lock_indicator.change_state()

            pygame.display.update()



    def on_loop(self):
        pass
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
