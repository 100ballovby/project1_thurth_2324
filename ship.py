import pygame as pg


class Ship:
    def __init__(self, settings, screen):
        """Инициализация корабля и задание начальной позиции"""
        self.screen = screen
        self.settings = settings

        # загрузка изображения корабля и получение его модели
        self.image = pg.image.load('images/ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # каждый корабль появляется у нижнего края экрана
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)  # сохранение вещественной координаты центра

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:  # если в параметре True
            self.rect.centerx += self.settings.ship_speed_factor
        elif self.moving_left and self.rect.left > 0:
            self.rect.centerx -= self.settings.ship_speed_factor
        elif self.moving_up and self.rect.top > 0:
            self.rect.centery -= self.settings.ship_speed_factor
        elif self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.centery += self.settings.ship_speed_factor

        #self.rect.centerx = self.center

    def blitme(self):
        """Рисует корабль в текущей позиции"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Размещает корабль посередине"""
        self.center = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom



