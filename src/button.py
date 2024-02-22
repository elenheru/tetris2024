import pygame as pg

from pygame.colordict import THECOLORS
from parameters import PARAMETERS


class Button:
    back_color = THECOLORS["black"]

    def __init__(self, text=None, color=None, assigned_key=None, origin=None, size=None):
        self.is_focused = None
        self.is_pressed = None
        self.is_inactive = None
        self.reset()

        if assigned_key is None:
            self.akey = pg.K_SPACE
        else:
            self.akey = assigned_key

        if text is None:
            self.text = "Button: pygame_ref_" + pg.key.name(self.akey)
        else:
            self.text = text

        if color is None:
            self.color = THECOLORS["grey50"]
        else:
            self.color = color

        if origin is None:
            self.origin = (0, 0)
        else:
            self.origin = origin

        if size is None:
            self.size = (
                PARAMETERS["resolution"][0] // 8,
                PARAMETERS["resolution"][1] // 16,
                )
        else:
            self.size = size

        self.f = PARAMETERS["pygame_font1"]

        self.sf_result = None
        self.sf_ready = pg.Surface(self.size)
        self._build_ready()

        self.sf_focused = pg.Surface(self.size)
        self._build_focused()

        self.sf_pressed = pg.Surface(self.size)
        self._build_pressed()

        self.sf_inactive = pg.Surface(self.size)
        self._build_inactive()

    def _build_inactive(self):
        self.sf_inactive.fill(THECOLORS["gray20"])
        pg.draw.rect(
            self.sf_inactive,
            self.color,
            self.sf_inactive.get_rect(),
            1
        )
        self.f.strikethrough = True
        fl = self.f.render(self.text, True, THECOLORS["gray30"])
        self.f.strikethrough = False
        place = fl.get_rect(center=(self.size[0] // 2, self.size[1] // 2))
        self.sf_inactive.blit(fl, place.topleft)

    def _build_ready(self):
        self.sf_ready.fill(Button.back_color)
        pg.draw.rect(
            self.sf_ready,
            self.color,
            self.sf_ready.get_rect(),
            1
        )
        fl = self.f.render(self.text, True, THECOLORS["white"])
        place = fl.get_rect(center=(self.size[0] // 2, self.size[1] // 2))
        self.sf_ready.blit(fl, place.topleft)

    def _build_focused(self):
        self.sf_focused.fill(Button.back_color)
        pg.draw.rect(
            self.sf_focused,
            self.color,
            self.sf_focused.get_rect(),
            4
        )
        fl = self.f.render(self.text, True, self.color)
        place = fl.get_rect(center=(self.size[0] // 2, self.size[1] // 2))
        self.sf_focused.blit(fl, place.topleft)

    def _build_pressed(self):
        self.sf_pressed.fill(self.color)
        self.f.underline = True
        fl = self.f.render(self.text, True, THECOLORS["black"])
        self.f.underline = False
        place = fl.get_rect(center=(self.size[0] // 2, self.size[1] // 2))
        self.sf_pressed.blit(fl, place.topleft)

    def prepare(self, pos, mouse_buttons_mask, keyboard_mask):

        if keyboard_mask[pg.K_RCTRL]:
            self.is_inactive = True
        else:
            self.is_inactive = False

        self.is_focused = True
        if pos[0] < self.origin[0]:
            self.is_focused = False
        if pos[1] < self.origin[1]:
            self.is_focused = False
        if pos[0] > self.origin[0] + self.size[0]:
            self.is_focused = False
        if pos[1] > self.origin[1] + self.size[1]:
            self.is_focused = False

        self.is_pressed = (keyboard_mask[self.akey]
                           or (self.is_focused and mouse_buttons_mask[0]))
        if self.is_inactive:
            self.sf_result = self.sf_inactive
        else:
            if self.is_pressed:
                self.sf_result = self.sf_pressed
            else:
                if self.is_focused:
                    self.sf_result = self.sf_focused
                else:
                    self.sf_result = self.sf_ready
        if self.is_inactive:
            self.is_focused = False
            self.is_pressed = False

    def reset(self):
        self.is_focused = False
        self.is_pressed = False
        self.is_inactive = False
