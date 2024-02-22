import pygame as pg
from pygame.colordict import THECOLORS
from button import Button
from parameters import PARAMETERS

from condition_over_to_terminal_src import ConditionOverToTerminal
from condition_over_to_main_menu_src import ConditionOverToMainMenu


class SiteOver:
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
                "MAIN MENU",
                THECOLORS["green"],
                pg.K_m,
                (1200, 300)
            ),
            Button(
                "the game is over",
                THECOLORS["tan" + "2"],
                pg.K_w,
                (850, 200)
            ),
        )
        self.conditions = (
            ConditionOverToTerminal(),
            ConditionOverToMainMenu(),
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
                        for b in self.buttons:
                            b.reset()
                        break

                    #  or we can update next site only once, if it is not identical
                    #  anyway all interface state has to be reset

    def _prepare_surface(self, tick, details, incoming):
        self.sf.fill(THECOLORS["black"])
        for b in self.buttons:
            b.prepare(incoming[1], incoming[2], incoming[3])
            self.sf.blit(b.sf_result, b.origin)
        #  score
        score_surface = \
            PARAMETERS["pygame_font1"].render(
                "Score : " + str(details["score"]),
                True,
                THECOLORS["orange"])
        self.sf.blit(score_surface, PARAMETERS["score_position"])