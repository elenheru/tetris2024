import pygame as pg

from parameters import PARAMETERS
from button import Button
from pygame.colordict import THECOLORS

from condition_main_menu_to_gaming_src import ConditionMainMenuToGaming
from condition_main_menu_to_settings import ConditionMainMenuToSettings
from condition_main_menu_to_terminal_src import ConditionMainMenuToTerminal


class SiteMainMenu:
    def __init__(self):
        if self.__class__.__name__ not in PARAMETERS["sites_names"]:
            raise Exception(self.__class__.__name__ + " is not in all-sites tuple")
        self.sf = pg.Surface(PARAMETERS["resolution"])
        self.next_site = None
        self.buttons = (
            Button(
                "QUIT GAME",
                THECOLORS["dodger" + "blue"],
                pg.K_q,
                (600, 700)
            ),
            Button(
                "NEW GAME",
                THECOLORS["green"],
                pg.K_n,
                (600, 300)
            ),
            Button(
                "SETTINGS",
                THECOLORS["orange"],
                pg.K_s,
                (600, 500)
            ),
        )
        self.conditions = (
            ConditionMainMenuToGaming(),
            ConditionMainMenuToSettings(),
            ConditionMainMenuToTerminal(),
        )

    def process(self, tick, details, incoming):
        self.next_site = self.__class__.__name__
        self._prepare_surface(tick, details, incoming)
        for c in self.conditions:
            condition_verdict = c.check(tick, details, incoming, self.buttons)
            if condition_verdict:
                c.treat(tick, details, incoming)
                if c.site_changer:
                    self.next_site = c.get_known_next_site()
                    if self.next_site != self.__class__.__name__:
                        break
        for b in self.buttons:
            b.reset()

    def _prepare_surface(self, tick, details, incoming):
        for b in self.buttons:
            b.prepare(incoming[1], incoming[2], incoming[3])
            self.sf.blit(b.sf_result, b.origin)
