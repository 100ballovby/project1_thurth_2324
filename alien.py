import pygame as pg
from pygame.sprite import Sprite


class Alien(Sprite):
    """Класс представляющий одного пришельца"""
    def __init__(self, settings, screen):
        """Инициализация пришельца"""
        super().__init__()
        self.screen = screen
        self.settings = settings

        # загрузка изображения
        self.image = pg.image.load('images/alien.png')
        self.rect = self.image.get_rect()

        # каждый новый пришелец будет появляться в верхнем левом углу экрана
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def blitme(self):
        """Вывод пришельца на экран"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Перемещает пришельца по экрану"""
        self.x += (self.settings.alien_speed_factor * self.settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        """Возвращает True, если пришелец находится у края экрана"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True


