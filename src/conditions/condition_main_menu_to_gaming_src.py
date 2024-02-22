import pygame as pg

from site_gaming_src import SiteGaming


class ConditionMainMenuToGaming:
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
        detailed_description["falling_figure"].clean_figure()
        self.next_site = SiteGaming.__name__

    def get_known_next_site(self):
        return self.next_site
