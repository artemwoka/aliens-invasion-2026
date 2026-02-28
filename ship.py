import pygame as pg
from pygame.sprite import Sprite


class Ship(Sprite):
    """Клас для керування кораблем"""

    def __init__(self, ai_game):
        """Ініціалізує корабель та встановлює його початкову позицію."""
        super().__init__()
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

    def center_ship(self):
        """Розміщує корабель по центру нижньої частини екрану."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
    
    def update(self):
        """Оновлює позицію корабля залежно від флагів переміщення."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        #Оновлює об'єкт rect на основі self.x
        self.rect.x = self.x