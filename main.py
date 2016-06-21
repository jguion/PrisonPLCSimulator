import pygame
from pygame.locals import *
import guard_station
import prison_cell

class App:
    def __init__(self):
        self._running = True
        self._screen = None
        self.size = self.weight, self.height = 1025, 700

    def on_init(self):
        pygame.init()
        self.font = pygame.font.SysFont('Times', 25)
        pygame.display.set_caption('Ybox Simulation')
        self._screen = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._screen.fill((black))

        x_padding = 50
        y_padding = 50

        cell_panel_width = 325
        cell_panel_heigh = 300

        guard_station_panel = guard_station.GuardStation(self._screen, self.font, 2, 50, 450)


        cell_one_panel = prison_cell.PrisonCell(self._screen, self.font, 1, x_padding, y_padding)
        cell_two_panel = prison_cell.PrisonCell(self._screen, self.font, 2, 2*x_padding+cell_panel_width, y_padding)

        pygame.display.update()
        self._running = True

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
    def on_loop(self):
        pass
    def on_render(self):
        pass
    def on_cleanup(self):
        pygame.quit()

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

    theApp = App()
    theApp.on_execute()
