from parameters import PARAMETERS
from constants_figure import figures_shapes_list


class ConditionFallingFigureAbsent:
    site_changer = False

    def __init__(self):
        self.next_site = None

    @staticmethod
    def check(tick, detailed_description, incoming, buttons):
        return not bool(detailed_description["falling_figure"].top_left_block_position)

    @staticmethod
    def treat(tick, detailed_description, incoming):
        if tick % PARAMETERS["step_time_divisor"] == 0:
            blocks = detailed_description["falling_figure"].build_complete_list_of_block_sets()
            for shape_number, block_set in enumerate(blocks):
                if not detailed_description["bulk"].check_collision(block_set):
                    detailed_description["falling_figure"].spawn_figure(figures_shapes_list[shape_number])
                    return None

    def get_known_next_site(self):
        if ConditionFallingFigureAbsent.site_changer:
            return self.next_site
        else:
            raise Exception(self.__class__.__name__ + "is not a site changer")
