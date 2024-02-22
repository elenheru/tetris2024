import pygame as pg


class ConditionFallingFigureMoveRequested:
    site_changer = False

    def __init__(self):
        self.next_site = None
        self.flag_left_move = None
        self.flag_right_move = None

    def check(self, tick, detailed_description, incoming, buttons):
        self.flag_left_move = False
        self.flag_right_move = False
        for e in incoming[0]:
            if e.type == pg.KEYDOWN:
                if e.key == pg.K_LEFT:
                    self.flag_left_move = True
                if e.key == pg.K_RIGHT:
                    self.flag_right_move = True
        return self.flag_right_move or self.flag_left_move

    def treat(self, tick, detailed_description, incoming):
        if detailed_description["falling_figure"].shape is None:
            return None
        if self.flag_right_move:
            position = (
                    detailed_description["falling_figure"].top_left_block_position[0] + 1,
                    detailed_description["falling_figure"].top_left_block_position[1]
                )
            blocks = detailed_description["falling_figure"].build_set_of_blocks(
                None,
                position,
                detailed_description["falling_figure"].orientation
            )
            may_move_right = not detailed_description["bulk"].check_collision(blocks)
            if may_move_right:
                detailed_description["falling_figure"].top_left_block_position = position
        if self.flag_left_move:
            position = (
                detailed_description["falling_figure"].top_left_block_position[0] - 1,
                detailed_description["falling_figure"].top_left_block_position[1]
            )
            blocks = detailed_description["falling_figure"].build_set_of_blocks(
                None,
                position,
                detailed_description["falling_figure"].orientation
            )
            may_move_left = not detailed_description["bulk"].check_collision(blocks)
            if may_move_left:
                detailed_description["falling_figure"].top_left_block_position = position

    def get_known_next_site(self):
        if ConditionFallingFigureMoveRequested.site_changer:
            return self.next_site
        else:
            raise Exception(self.__class__.__name__ + "is not a site changer")
