import pygame as pg

from pygame.colordict import THECOLORS
from parameters import PARAMETERS
from button import Button

from condition_settings_to_terminal_src import ConditionSettingsToTerminal
from condition_settings_to_main_menu_src import ConditionSettingsToMainMenu


class SiteSettings:
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
                "no setting yet",
                THECOLORS["tan" + "4"],
                pg.K_w,
                (850, 200)
            ),
            Button(
                "MAIN MENU",
                THECOLORS["green"],
                pg.K_m,
                (600, 100)
            ),
        )
        self.conditions = (
            ConditionSettingsToTerminal(),
            ConditionSettingsToMainMenu(),
        )
        self.is_not_complete = True
        #  what settings can be there

    def process(self, tick, details, incoming):
        self.next_site = self.__class__.__name__
        self._prepare_surface(tick, details, incoming)
        for c in self.conditions:
            condition_verdict = c.check(tick, details, incoming, self.buttons)
            if condition_verdict:
                c.treat(tick, details, incoming)
                if c.site_changer:
                    self.next_site = c.get_known_next_site()
        for b in self.buttons:
            b.reset()

    def _prepare_surface(self, tick, details, incoming):
        if self.is_not_complete:
            self.buttons[1].text = str(tick)
            self.buttons[1]._build_ready()

        for b in self.buttons:
            b.prepare(incoming[1], incoming[2], incoming[3])
            self.sf.blit(b.sf_result, b.origin)

