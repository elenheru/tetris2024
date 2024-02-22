from parameters import PARAMETERS
from constants_figure import figures_colors


class ConditionAttachToBulkNeeded:
    site_changer = False

    def __init__(self):
        self.next_site = None

    @staticmethod
    def check(tick, detailed_description, incoming, buttons):
        return detailed_description["falling_figure"].attach_requested

    @staticmethod
    def treat(tick, detailed_description, incoming):
        blocks = detailed_description["falling_figure"].build_set_of_blocks(
            None,
            None,
            None
        )
        color = figures_colors[detailed_description["falling_figure"].shape]
        for b in blocks:
            detailed_description["bulk"].join_block(b, color)

        detailed_description["falling_figure"].clean_figure()

    def get_known_next_site(self):
        if ConditionAttachToBulkNeeded.site_changer:
            return self.next_site
        else:
            raise Exception(self.__class__.__name__ + "is not a site changer")
