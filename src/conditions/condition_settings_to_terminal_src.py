import pygame as pg

from site_terminal_src import SiteTerminal


class ConditionSettingsToTerminal:
    def __init__(self):
        self.next_site = None
        self.site_changer = True

    @staticmethod
    def check(tick, detailed_description, incoming, buttons):
        if buttons[0].is_pressed:
            return True
        else:
            return False

    def treat(self, tick, detailed_description, incoming):
        self.next_site = SiteTerminal.__name__

    def get_known_next_site(self):
        return self.next_site
