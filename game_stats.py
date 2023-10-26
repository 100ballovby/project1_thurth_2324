class GameStats:
    """Отслеживание статистики"""
    def __init__(self, settings):
        """Инициализация статистики"""
        self.settings = settings
        self.game_active = True  # игра изначально активна
        self.reset_stats()

    def reset_stats(self):
        """Инициализирует статистики, изменяющуюся в ходе игры"""
        self.ships_left = self.settings.ship_limit

