import pygame as pg


class Ship:
    """Клас для керування кораблем"""

    def __init__(self, ai_game):
        """Ініціалізує корабель та встановлює його початкову позицію."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        #Завантажує зображення корабля та отримує його прямокутник.
        self.image = pg.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        #Кожен новий корабель з'являється внизу посередині екрану.
        self.rect.midbottom = self.screen_rect.midbottom

        #Дробова координата центру корабля
        self.x = float(self.rect.x)

        #Флаг переміщення корабля
        self.moving_right = False
        self.moving_left = False
    
    def blitme(self):
        """Відображає корабель у поточній позиції."""
        self.screen.blit(self.image, self.rect)
    
    def update(self):
        """Оновлює позицію корабля залежно від флагів переміщення."""
        if self.moving_right:
            self.x += self.settings.ship_speed
        if self.moving_left:
            self.x -= self.settings.ship_speed

        #Оновлює об'єкт rect на основі self.x
        self.rect.x = self.x