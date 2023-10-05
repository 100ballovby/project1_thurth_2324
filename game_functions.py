import sys
import pygame as pg


def check_keydown_events(event, ship):
    """Реагирует на нажатие кнопок на клавиатуре"""
    if event.key == pg.K_RIGHT:
        ship.moving_right = True
    elif event.key == pg.K_LEFT:
        ship.moving_left = True


def check_keyup_events(event, ship):
    if event.key == pg.K_RIGHT:
        ship.moving_right = False
    elif event.key == pg.K_LEFT:
        ship.moving_left = False


def check_events(ship):
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
        elif event.type == pg.KEYDOWN:
            check_keydown_events(event, ship)
        elif event.type == pg.KEYUP:
            check_keyup_events(event, ship)


def update_screen(settings, screen, ship):
    screen.fill(settings.bg_color)
    ship.blitme()
    pg.display.flip()
