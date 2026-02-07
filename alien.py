import pygame as pg
import pygame.sprite as sprite


class Alien(sprite.Sprite):
    """Клас для прибульця"""

    def __init__(self, ai_game):
        """Ініціалізує прибульця та встановлює його початкову позицію."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Завантажує зображення прибульця та отримує його rect.
        self.image = pg.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Кожен новий прибулець з'являється у верхньому лівому куті екрану.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Зберігає точну горизонтальну позицію прибульця.
        self.x = float(self.rect.x)

    def update(self):
        """Рухає прибульця вправо."""
        self.x += self.settings.alien_speed
        self.rect.x = self.x