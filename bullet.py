import pygame as pg
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Клас для керування снарядами якими стріляє корабель."""

    def __init__(self, ai_game):
        """Створює снаряд у поточній позиції корабля."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        #Створює снаряд у позиції (0,0) та потім встановлює правильну позицію.
        self.rect = pg.Rect(0, 0, self.settings.bullet_width,
                            self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        #Зберігає позицію снаряда як десяткове значення.
        self.y = float(self.rect.y)