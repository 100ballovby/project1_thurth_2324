import sys
import pygame as pg
from bullet import Bullet


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """Реагирует на нажатие кнопок на клавиатуре"""
    if event.key == pg.K_RIGHT:
        ship.moving_right = True
    elif event.key == pg.K_LEFT:
        ship.moving_left = True
    elif event.key == pg.K_SPACE:
        # создаем новую пулю и добавляем ее в группу с пулями
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def check_keyup_events(event, ship):
    if event.key == pg.K_RIGHT:
        ship.moving_right = False
    elif event.key == pg.K_LEFT:
        ship.moving_left = False


def check_events(ai_settings, screen, ship, bullets):
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
        elif event.type == pg.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pg.KEYUP:
            check_keyup_events(event, ship)


def update_screen(settings, screen, ship, bullets):
    screen.fill(settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    pg.display.flip()
