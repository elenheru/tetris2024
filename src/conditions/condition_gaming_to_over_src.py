#  from site_over_src import SiteOver
from parameters import PARAMETERS


class ConditionGamingToOver:
    def __init__(self):
        self.next_site = None
        self.site_changer = True

    @staticmethod
    def check(tick, detailed_description, incoming, buttons):
        if buttons[0].is_pressed:
            return True
        if not detailed_description["falling_figure"].top_left_block_position:
            blocks = detailed_description["falling_figure"].build_complete_list_of_block_sets()
            for block_set in blocks:
                if not detailed_description["bulk"].check_collision(block_set):
                    return False
            return True
        return False

    def treat(self, tick, detailed_description, incoming):
        self.next_site = PARAMETERS["sites_names"][5]

    def get_known_next_site(self):
        if self.site_changer:
            return self.next_site
        else:
            raise Exception(self.__class__.__name__ + "is not a site changer")
