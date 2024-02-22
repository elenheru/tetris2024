import pygame as pg

from site_settings_src import SiteSettings


class ConditionMainMenuToSettings:
    def __init__(self):
        self.next_site = None
        self.site_changer = True

    @staticmethod
    def check(tick, detailed_description, incoming, buttons):
        if buttons[2].is_pressed:
            return True
        else:
            return False

    def treat(self, tick, detailed_description, incoming):
        self.next_site = SiteSettings.__name__

    def get_known_next_site(self):
        return self.next_site
