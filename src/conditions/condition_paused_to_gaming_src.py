#  from site_gaming_src import SiteGaming
from parameters import PARAMETERS


class ConditionPausedToGaming:
    def __init__(self):
        self.next_site = None
        self.site_changer = True

    @staticmethod
    def check(tick, detailed_description, incoming, buttons):
        if buttons[1].is_pressed:
            return True
        else:
            return False

    def treat(self, tick, detailed_description, incoming):
        self.next_site = PARAMETERS["sites_names"][3]

    def get_known_next_site(self):
        if self.site_changer:
            return self.next_site
        else:
            raise Exception(self.__class__.__name__ + "is not a site changer")
