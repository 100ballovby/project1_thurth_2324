import pygame as pg


class Ship:
    def __init__(self, screen):
        """Инициализация корабля и задание начальной позиции"""
        self.screen = screen

        # загрузка изображения корабля и получение его модели
        self.image = pg.image.load('ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # каждый корабль появляется у нижнего края экрана
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """Рисует корабль в текущей позиции"""
        self.screen.blit(self.image, self.rect)



