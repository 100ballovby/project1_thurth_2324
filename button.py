import pygame.font as pf
import pygame as pg


class Button:
    def __init__(self, settings, screen, msg):
        """Инициализация атрибутов кнопки"""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # назначение размеров и свойств кнопки
        self.width, self.height = 200, 50
        self.color = (0, 255, 120)
        self.text_color = (0, 0, 0)
        self.font = pf.SysFont('Arial', 48)

        # построение объекта
        self.rect = pg.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # сообщение на кнопке
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """Преобразуем msg в прямоугольник и выравниваем текст"""
        self.message = self.font.render(msg, True, self.text_color, self.color)
        self.message_rect = self.message.get_rect()
        self.message_rect.center = self.rect.center

    def draw_button(self):
        """Отображение кнопки на экране"""
        self.screen.fill(self.color, self.rect)
        self.screen.blit(self.message, self.message_rect)



