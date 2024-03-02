import pygame as pg

from pygame.colordict import THECOLORS
from button import Button
from parameters import PARAMETERS
from constants_figure import figures_colors

from condition_paused_to_over_src import ConditionPausedToOver
from condition_paused_to_gaming_src import ConditionPausedToGaming


class SitePaused:
    def __init__(self):
        if self.__class__.__name__ not in PARAMETERS["sites_names"]:
            raise Exception(self.__class__.__name__ + " is not in all-sites tuple")
        self.sf = pg.Surface(PARAMETERS["resolution"])
        self.next_site = None
        self.buttons = (
            Button(
                "MAKE GAME OVER",
                THECOLORS["fire" + "brick"],
                pg.K_BACKSPACE,
                (1200, 100)
            ),
            Button(
                "RESUME GAME",
                THECOLORS["medium" + "orchid"],
                pg.K_r,
                (1200, 800)
            ),
        )
        self.conditions = (
            ConditionPausedToOver(),
            ConditionPausedToGaming(),
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

    def _prepare_surface(self, tick, details, incoming):
        self.sf.fill(THECOLORS["grey3"])
        for b in self.buttons:
            b.prepare(incoming[1], incoming[2], incoming[3])
            self.sf.blit(b.sf_result, b.origin)

        if not details["falling_figure"].top_left_block_position is None:
            falling_figure_blocks = details["falling_figure"].build_set_of_blocks(
                None,
                None,
                None
            )
            for block in falling_figure_blocks:
                block_rectangle = \
                    tuple((
                        PARAMETERS["playground_right_shift_px"] + block[0] * details["bulk"].block_size,
                        block[1] * details["bulk"].block_size,
                        details["bulk"].block_size,
                        details["bulk"].block_size
                    ))
                pg.draw.rect(self.sf,
                             THECOLORS["grey20"],
                             block_rectangle,
                             0,
                             5, 5, 5, 5
                             )

        for ix in range(details["bulk"].field_size[0]):
            for iy in range(details["bulk"].field_size[1]):
                block_rectangle = \
                    tuple((
                        PARAMETERS["playground_right_shift_px"] + ix * details["bulk"].block_size,
                        iy * details["bulk"].block_size,
                        details["bulk"].block_size,
                        details["bulk"].block_size
                    ))
                if details["bulk"].occupation_mask[ix][iy]:
                    pg.draw.rect(self.sf,
                                 THECOLORS["grey20"],
                                 block_rectangle
                                 )
                pg.draw.rect(self.sf,
                             details["bulk"].__class__.grid_color,
                             block_rectangle,
                             1
                             )

        #  score
        score_surface = \
            PARAMETERS["pygame_font1"].render(
                "Score : " + str(details["score"]),
                True,
                THECOLORS["orange"])

        self.sf.blit(score_surface, PARAMETERS["score_position"])
