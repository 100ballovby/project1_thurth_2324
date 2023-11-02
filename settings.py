class Settings:
    def __init__(self):
        """Инициализация настроек игры"""
        # параметры экрана игры
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed_factor = 1.5
        self.ship_limit = 3  # доступно 3 корабля в игре

        # параметры снаряда
        self.bullet_speed = 3
        self.bullet_width = 3
        self.bullet_height = 20
        self.bullet_color = (210, 87, 247)
        self.bullets_allowed = 3

        # параметры флота
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        self.fleet_direction = 1  # направление движения 1 - вправо, -1 - влево

        # ускорение игры
        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 1.5
        self.bullet_speed = 3
        self.alien_speed_factor = 1
        self.fleet_direction = 1

    def increase_speed(self):
        """Увеличивает настройки скорости"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
