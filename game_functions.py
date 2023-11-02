import sys
import pygame as pg
from bullet import Bullet
from alien import Alien
from time import sleep


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


def check_events(ai_settings, screen, ship, bullets, stats, play_button, aliens):
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
        elif event.type == pg.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pg.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pg.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pg.mouse.get_pos()
            check_play_button(stats, play_button, mouse_x, mouse_y, ai_settings, screen, ship, aliens, bullets)


def check_play_button(stats, play_button, mouse_x, mouse_y, settings, screen, ship, aliens, bullets):
    """Запускает игру по нажатию кнопки Play"""
    if play_button.rect.collidepoint(mouse_x, mouse_y):
        stats.reset_stats()
        stats.game_active = True

        aliens.empty()
        bullets.empty()

        create_fleet(settings, screen, aliens, ship)
        ship.center_ship()


def update_screen(settings, screen, ship, bullets, aliens, stats, play_button):
    screen.fill(settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)

    if not stats.game_active:
        play_button.draw_button()

    pg.display.flip()


def update_bullets(bullets, aliens, settings, screen, ship):
    # удаление пуль, вышедших за пределы экрана
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:  # если пуля вышла за пределы экрана
            bullets.remove(bullet)
    check_bullet_alien_collisions(settings, screen, ship, aliens, bullets)


def check_bullet_alien_collisions(settings, screen, ship, aliens, bullets):
    """Обнаружение попадания в пришельца"""
    collisions = pg.sprite.groupcollide(bullets, aliens, True, True)
    if len(aliens) == 0:
        # уничтожаем существующие пули и добавляем новый флот
        bullets.empty()
        create_fleet(settings, screen, aliens, ship)


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


def update_alien(settings, aliens, ship, stats, screen, bullets):
    """Перемещение пришельцев"""
    check_fleet_edges(settings, aliens)
    aliens.update()

    if pg.sprite.spritecollideany(ship, aliens):
        ship_hit(settings, stats, screen, ship, aliens, bullets)
    check_aliens_bottom(settings, stats, screen, ship, aliens, bullets)


def check_fleet_edges(settings, aliens):
    """Реагирует на достижение пришельцем края экрана"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(settings, aliens)
            break


def change_fleet_direction(settings, aliens):
    """Опускает флот и меняет направление"""
    for alien in aliens.sprites():
        alien.rect.y += settings.fleet_drop_speed
    settings.fleet_direction *= -1


def ship_hit(settings, stat, screen, ship, aliens, bullets):
    """Обрабатываем столкновения пришельцев с кораблем"""
    if stat.ships_left > 0:
        stat.ships_left -= 1  # уменьшаем количество кораблей
        # убираем пули и пришельцев
        aliens.empty()
        bullets.empty()
        # создаем флот и центруем корабль
        create_fleet(settings, screen, aliens, ship)
        ship.center_ship()

        # пауза 0.5 секунды
        sleep(0.5)
    else:
        stat.game_active = False


def check_aliens_bottom(settings, stats, screen, ship, aliens, bullets):
    """Проверяет, достигли ли пришельцы нижнего края экрана"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # происходит то же самое, что и при столкновении с кораблем
            ship_hit(settings, stats, screen, ship, aliens, bullets)
            break
