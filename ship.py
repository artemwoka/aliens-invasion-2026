import pygame as pg


class Ship:
    """Клас для керування кораблем"""

    def __init__(self, ai_game):
        """Ініціалізує корабель та встановлює його початкову позицію."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #Завантажує зображення корабля та отримує його прямокутник.
        self.image = pg.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        #Кожен новий корабель з'являється внизу посередині екрану.
        self.rect.midbottom = self.screen_rect.midbottom
    
    def blitme(self):
        """Відображає корабель у поточній позиції."""
        self.screen.blit(self.image, self.rect)