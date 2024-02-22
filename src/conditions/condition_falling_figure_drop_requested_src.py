import pygame as pg


class ConditionFallingFigureDropRequested:
    site_changer = False

    def __init__(self):
        self.next_site = None

    @staticmethod
    def check(tick, detailed_description, incoming, buttons):
        for e in incoming[0]:
            if e.type == pg.KEYDOWN and e.key == pg.K_PAGEDOWN:
                return True

    @staticmethod
    def treat(tick, detailed_description, incoming):
        if detailed_description["falling_figure"].shape is None:
            return None
        tested_position = (
            detailed_description["falling_figure"].top_left_block_position[0],
            detailed_description["falling_figure"].top_left_block_position[1] + 1
        )

        while True:
            blocks = detailed_description["falling_figure"].build_set_of_blocks(
                None,
                tested_position,
                detailed_description["falling_figure"].orientation
            )
            may_step_down = not detailed_description["bulk"].check_collision(blocks)
            if may_step_down:
                tested_position = (tested_position[0], tested_position[1] + 1)
            else:
                detailed_description["falling_figure"].attach_requested = True
                detailed_description["falling_figure"].top_left_block_position = (
                    tested_position[0], tested_position[1] - 1
                )
                break

    def get_known_next_site(self):
        if ConditionFallingFigureDropRequested.site_changer:
            return self.next_site
        else:
            raise Exception(self.__class__.__name__ + "is not a site changer")
