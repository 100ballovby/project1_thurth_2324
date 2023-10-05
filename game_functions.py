import sys
import pygame as pg


def check_events(ship):
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_RIGHT:
                ship.moving_right = True
            elif event.key == pg.K_LEFT:
                ship.moving_left = True
        elif event.type == pg.KEYUP:
            if event.key == pg.K_RIGHT:
                ship.moving_right = False
            elif event.key == pg.K_LEFT:
                ship.moving_left = False


def update_screen(settings, screen, ship):
    screen.fill(settings.bg_color)
    ship.blitme()
    pg.display.flip()
