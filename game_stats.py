class GameStats:
    """Відстежує статистику гри."""

    def __init__(self, ai_game):
        """Ініціалізує статистику."""
        self.settings = ai_game.settings
        self.reset_stats()

        # Гра запускається в активному стані.
        self.game_active = True

        # Рекорд не повинен скидатися.
        self.high_score = 0

    def reset_stats(self):
        """Ініціалізує статистику, яка може змінюватися впродовж гри."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
