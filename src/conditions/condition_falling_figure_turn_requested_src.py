import pygame as pg
from constants_figure import figures_structures


class ConditionFallingFigureTurnRequested:
    site_changer = False

    def __init__(self):
        self.next_site = None

    @staticmethod
    def check(tick, detailed_description, incoming, buttons):
        for e in incoming[0]:
            if e.type == pg.KEYDOWN and e.key == pg.K_UP:
                return True
        return False

    @staticmethod
    def treat(tick, detailed_description, incoming):
        if detailed_description["falling_figure"].shape is None:
            return None
        orientations_amount = len(figures_structures[detailed_description["falling_figure"].shape])
        blocks = detailed_description["falling_figure"].build_set_of_blocks(
            None,
            None,
            (detailed_description["falling_figure"].orientation + 1) % orientations_amount
        )
        may_turn = not detailed_description["bulk"].check_collision(blocks)
        if may_turn:
            detailed_description["falling_figure"].orientation = \
                (detailed_description["falling_figure"].orientation + 1) % orientations_amount

    def get_known_next_site(self):
        if ConditionFallingFigureTurnRequested.site_changer:
            return self.next_site
        else:
            raise Exception(self.__class__.__name__ + "is not a site changer")
