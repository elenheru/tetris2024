import pygame as pg

from parameters import PARAMETERS
from site_main_menu_src import SiteMainMenu


class SiteInitial:
    def __init__(self):
        if self.__class__.__name__ not in PARAMETERS["sites_names"]:
            raise Exception(self.__class__.__name__ + " is not in all-sites tuple")
        self.sf = pg.Surface(PARAMETERS["resolution"])
        self.next_site = None

    def process(self, tick, details, incoming):
        self.next_site = SiteMainMenu.__name__
        #  TODO: add condition (which is always true) to go to main menu

    def _prepare_surface(self):
        pass
