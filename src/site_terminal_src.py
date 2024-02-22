import pygame as pg

from parameters import PARAMETERS


class SiteTerminal:
    def __init__(self):
        self.sf = pg.Surface(PARAMETERS["resolution"])
        self.next_site = None
        self.buttons = ()
        self.conditions = ()

    def process(self, tick, details, incoming):
        self.next_site = SiteTerminal.__name__

    def _prepare_surface(self):
        pass
