import pygame as pg
from pygame.font import SysFont

pg.init()
PARAMETERS = dict()

PARAMETERS["resolution"] = (1440, 1080)
PARAMETERS["FPS"] = 24  # 60
PARAMETERS["fading_time_frames"] = 10
PARAMETERS["score_position"] = (1200, 50)

PARAMETERS["playground_width"] = 10
PARAMETERS["playground_height"] = 19

PARAMETERS["block_size"] = min(
            PARAMETERS["resolution"][0] // PARAMETERS["playground_width"],
            PARAMETERS["resolution"][1] // PARAMETERS["playground_height"]
        )
PARAMETERS["playground_right_shift_px"] = \
    (
            PARAMETERS["resolution"][0]
            - PARAMETERS["block_size"] * PARAMETERS["playground_width"]
    ) // 2

PARAMETERS["step_time_divisor"] = 40

PARAMETERS["sites_names"] = (
    "SiteInitial",
    "SiteMainMenu",
    "SiteSettings",
    "SiteGaming",
    "SitePaused",
    "SiteOver",
    "SiteTerminal"
)

PARAMETERS["font1_name"] = "tahoma"
PARAMETERS["font1_size"] = 18
PARAMETERS["pygame_font1"] = SysFont(
    PARAMETERS["font1_name"],
    PARAMETERS["font1_size"]
)
