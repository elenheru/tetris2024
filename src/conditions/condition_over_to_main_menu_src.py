#  from site_main_menu_src import SiteMainMenu
from parameters import PARAMETERS


class ConditionOverToMainMenu:
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
        detailed_description["bulk"].clean_bulk()
        self.next_site = PARAMETERS["sites_names"][1]

    def get_known_next_site(self):
        if self.site_changer:
            return self.next_site
        else:
            raise Exception(self.__class__.__name__ + "is not a site changer")