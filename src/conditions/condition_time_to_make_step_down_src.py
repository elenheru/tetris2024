from parameters import PARAMETERS


class ConditionTimeToMakeStepDown:
    site_changer = False

    def __init__(self):
        self.next_site = None

    @staticmethod
    def check(tick, detailed_description, incoming, buttons):
        divisor = max(PARAMETERS["step_time_divisor"] - (detailed_description["score"] // 10),
                      PARAMETERS["step_time_divisor"] // 2)
        return tick % divisor == divisor // 2

    @staticmethod
    def treat(tick, detailed_description, incoming):
        if detailed_description["falling_figure"].shape is None:
            return None
        tested_position = (
            detailed_description["falling_figure"].top_left_block_position[0],
            detailed_description["falling_figure"].top_left_block_position[1] + 1
        )
        blocks = detailed_description["falling_figure"].build_set_of_blocks(
            None,
            tested_position,
            detailed_description["falling_figure"].orientation
        )
        may_step_down = not detailed_description["bulk"].check_collision(blocks)
        if may_step_down:
            detailed_description["falling_figure"].top_left_block_position = \
                tested_position
        else:
            detailed_description["falling_figure"].attach_requested = True

    def get_known_next_site(self):
        if ConditionTimeToMakeStepDown.site_changer:
            return self.next_site
        else:
            raise Exception(self.__class__.__name__ + "is not a site changer")
