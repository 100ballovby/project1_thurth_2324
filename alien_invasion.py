import pygame as pg
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group


def run_game(window_name):
    pg.init()
    ai_settings = Settings()
    screen = pg.display.set_mode((ai_settings.screen_width,
                                  ai_settings.screen_height))
    pg.display.set_caption(window_name)

    ship = Ship(ai_settings, screen)
    bullets = Group()  # создаем список пуль
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)  # отслеживание событий мыши и клавиатуры
        ship.update()  # постоянное опрашивает экземпляр класса Ship
        bullets.update()
        # удаление пуль, вышедших за пределы экрана
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:  # если пуля вышла за пределы экрана
                bullets.remove(bullet)
        gf.update_screen(ai_settings, screen, ship, bullets)


run_game('Alien invasion game')
