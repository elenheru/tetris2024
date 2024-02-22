import pygame as pg
from pygame.colordict import THECOLORS

from parameters import PARAMETERS
from constants_figure import figures_colors
from button import Button

from condition_gaming_to_paused_src import ConditionGamingToPaused
from condition_gaming_to_over_src import ConditionGamingToOver

from condition_line_completed_src import ConditionLineCompleted
from condition_falling_figure_absent_src import ConditionFallingFigureAbsent
from condition_falling_figure_move_requested_src import ConditionFallingFigureMoveRequested
from condition_falling_figure_turn_requested_src import ConditionFallingFigureTurnRequested
from condition_falling_figure_drop_requested_src import ConditionFallingFigureDropRequested
from condition_time_to_make_step_down_src import ConditionTimeToMakeStepDown
from condition_attach_needed_src import ConditionAttachToBulkNeeded


class SiteGaming:
    def __init__(self):
        if self.__class__.__name__ not in PARAMETERS["sites_names"]:
            raise Exception(self.__class__.__name__ + " is not in all-sites tuple")
        self.sf = pg.Surface(PARAMETERS["resolution"])
        self.next_site = None
        self.buttons = (
            Button(
                "MAKE GAME OVER",
                THECOLORS["fire" + "brick"],
                pg.K_f,
                (1200, 100)
            ),
            Button(
                "PAUSE GAME",
                THECOLORS["dark" + "magenta"],
                pg.K_p,
                (1200, 1000)
            ),
        )
        self.conditions = (
            ConditionFallingFigureAbsent(),
            ConditionGamingToOver(),
            ConditionGamingToPaused(),
            ConditionLineCompleted(),
            ConditionFallingFigureMoveRequested(),
            ConditionFallingFigureTurnRequested(),
            ConditionFallingFigureDropRequested(),
            ConditionTimeToMakeStepDown(),
            ConditionAttachToBulkNeeded(),
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
        self.sf.fill(THECOLORS["black"])

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
                             figures_colors[details["falling_figure"].shape],
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
                                 details["bulk"].color_mask[ix][iy],
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
        # TODO highlight place where the figure is falling to