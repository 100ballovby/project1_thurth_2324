class Settings:
    def __init__(self):
        """Инициализация настроек игры"""
        # параметры экрана игры
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed_factor = 1.5

        # параметры снаряда
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 20
        self.bullet_color = (210, 87, 247)
        self.bullets_allowed = 3

        # параметры флота
        self.alien_speed_factor = 1


