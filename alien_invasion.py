import pygame as pg
from settings import Settings
from ship import Ship
import game_functions as gf


def run_game(window_name):
    pg.init()
    ai_settings = Settings()
    screen = pg.display.set_mode((ai_settings.screen_width,
                                  ai_settings.screen_height))
    pg.display.set_caption(window_name)

    ship = Ship(ai_settings, screen)
    while True:
        gf.check_events(ship)  # отслеживание событий мыши и клавиатуры
        ship.update()  # постоянное опрашивает экземпляр класса Ship
        gf.update_screen(ai_settings, screen, ship)


run_game('Alien invasion game')
