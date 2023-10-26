import sys
import pygame as pg
from bullet import Bullet
from alien import Alien


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """Реагирует на нажатие кнопок на клавиатуре"""
    if event.key == pg.K_RIGHT:
        ship.moving_right = True
    elif event.key == pg.K_LEFT:
        ship.moving_left = True
    elif event.key == pg.K_UP:
        ship.moving_up = True
    elif event.key == pg.K_DOWN:
        ship.moving_down = True
    elif event.key == pg.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pg.K_q:  # для быстрого выхода из игры
        sys.exit()


def check_keyup_events(event, ship):
    if event.key == pg.K_RIGHT:
        ship.moving_right = False
    elif event.key == pg.K_LEFT:
        ship.moving_left = False
    elif event.key == pg.K_UP:
        ship.moving_up = False
    elif event.key == pg.K_DOWN:
        ship.moving_down = False


def check_events(ai_settings, screen, ship, bullets):
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
        elif event.type == pg.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pg.KEYUP:
            check_keyup_events(event, ship)


def update_screen(settings, screen, ship, bullets, aliens):
    screen.fill(settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    pg.display.flip()


def update_bullets(bullets):
    # удаление пуль, вышедших за пределы экрана
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:  # если пуля вышла за пределы экрана
            bullets.remove(bullet)


def fire_bullet(ai_settings, screen, ship, bullets):
    # создаем новую пулю и добавляем ее в группу с пулями
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def get_number_rows(settings, ship_height, alien_height):
    """Определяет количество рядов, помещающихся на экране"""
    available_space_y = (settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def get_number_aliens_x(settings, alien_width):
    available_space_x = settings.screen_width - 2 * alien_width
    number_of_aliens = int(available_space_x / (2 * alien_width))
    return number_of_aliens


def create_alien(settings, screen, aliens, alien_number, row_number):
    alien = Alien(settings, screen)
    alien_width = alien.rect.width
    alien_height = alien.rect.height
    alien.x = alien_width + (2 * alien_width) * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien_height + (2 * alien_height) * row_number
    aliens.add(alien)


def create_fleet(settings, screen, aliens, ship):
    """Создает флот пришельцев"""
    # Интервал между соседними пришельцами равен одной ширине пришельца
    alien = Alien(settings, screen)
    number_aliens_x = get_number_aliens_x(settings, alien.rect.width)
    number_rows = get_number_rows(settings, ship.rect.height, alien.rect.height)

    # создаем первый ряд пришельцев
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            # создание пришельца и размещение его в ряду
            create_alien(settings, screen, aliens, alien_number, row_number)


def update_alien(aliens):
    """Перемещение пришельцев"""
    aliens.update()
