import sys
import pygame as pg
from settings import Settings
from ship import Ship


def run_game(window_name):
    pg.init()
    ai_settings = Settings()
    screen = pg.display.set_mode((ai_settings.screen_width,
                                  ai_settings.screen_height))
    pg.display.set_caption(window_name)

    ship = Ship(screen)
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
        screen.fill(ai_settings.bg_color)
        ship.blitme()
        pg.display.flip()


run_game('Alien invasion game')
