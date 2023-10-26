import pygame as pg
from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf
from pygame.sprite import Group


def run_game(window_name):
    pg.init()
    ai_settings = Settings()
    screen = pg.display.set_mode((ai_settings.screen_width,
                                  ai_settings.screen_height))
    pg.display.set_caption(window_name)

    ship = Ship(ai_settings, screen)
    aliens = Group()  # создаем список пришельцев
    gf.create_fleet(ai_settings, screen, aliens, ship)
    bullets = Group()  # создаем список пуль
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)  # отслеживание событий мыши и клавиатуры
        ship.update()  # постоянное опрашивает экземпляр класса Ship
        bullets.update()
        gf.update_bullets(bullets, aliens, ai_settings, screen, ship)
        gf.update_alien(ai_settings, aliens)
        gf.update_screen(ai_settings, screen, ship, bullets, aliens)


run_game('Alien invasion game')
