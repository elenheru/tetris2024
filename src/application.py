import pygame as pg
import sys

from src.parameters import PARAMETERS
from site_initial_src import SiteInitial
from site_main_menu_src import SiteMainMenu
from site_settings_src import SiteSettings
from site_gaming_src import SiteGaming
from site_paused_src import SitePaused
from site_over_src import SiteOver
from site_terminal_src import SiteTerminal

from detail_falling_figure_src import FallingFigure
from detail_bulk_src import Bulk


class Application:
    def __init__(self):
        self.tick_value = 0
        self.is_running = True
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode(PARAMETERS["resolution"], pg.NOFRAME)
        self.current_site_name = PARAMETERS["sites_names"][0]
        self.target_site_name = None
        self.sites = {
            SiteInitial.__name__: SiteInitial(),
            SiteMainMenu.__name__: SiteMainMenu(),
            SiteSettings.__name__: SiteSettings(),
            SiteGaming.__name__: SiteGaming(),
            SitePaused.__name__: SitePaused(),
            SiteOver.__name__: SiteOver(),
            SiteTerminal.__name__: SiteTerminal()
        }
        self.details = {
            "score": 0,
            "falling_figure": FallingFigure(),
            "bulk": Bulk()
        }

    def run(self):
        while self.is_running:
            self.tick_value += 1

            incoming = (
                pg.event.get(),
                pg.mouse.get_pos(),
                pg.mouse.get_pressed(),
                pg.key.get_pressed()
            )

            for e in incoming[0]:
                if e.type == pg.QUIT:
                    self.is_running = False

            self.sites[self.current_site_name].process(
                self.tick_value,
                self.details,
                incoming
            )

            self.target_site_name = self.sites[self.current_site_name].next_site
            self.sites[self.current_site_name].next_site = self.current_site_name

            if self.current_site_name == SiteTerminal.__name__:
                self.is_running = False
                continue

            self.screen.blit(self.sites[self.current_site_name].sf, (0, 0))
            pg.display.update()

            self.current_site_name = self.target_site_name

            self.clock.tick(PARAMETERS["FPS"])

    @staticmethod
    def quit():
        pg.quit()
        sys.exit()
