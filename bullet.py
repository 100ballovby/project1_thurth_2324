import pygame as pg
from pygame.sprite import Sprite


class Bullet(Sprite):
    """класс для управления пулями"""
    def __init__(self, ai_settings, screen, ship):
        """Создаю объекты пули в текущей позиции корабля """
        super().__init__()
        self.screen = screen

        '''self.rect = pg.Rect(0, 0, ai_settings.bullet_width,
                            ai_settings.bullet_height)  # устанавливаю пулю в координате 0,0'''
        self.image = pg.image.load('images/bullet_s.png').convert_alpha()
        self.rect = self.image.get_rect()  # пространство для пули берется с картинки
        self.rect.centerx = ship.rect.centerx  # перемещаю центр пули к кораблю
        self.rect.top = ship.rect.top  # и "приклеиваю" пулю к верхней части корабля

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed

        self.y = self.rect.y

    def update(self):
        """Перемещает пулю по экрану"""
        self.y -= self.speed_factor
        self.rect.y = self.y  # чтобы квадрат перемещался вместе с пулей

    def draw_bullet(self):
        """Вывод пули на экран"""
        self.screen.blit(self.image, self.rect)  # отрисовываем
        #pg.draw.rect(self.screen, self.color, self.rect)

