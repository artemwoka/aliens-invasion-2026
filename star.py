import random

import pygame as pg
from pygame.sprite import Sprite


class Star(Sprite):
    """Клас для виведення зірок на фоні гри."""
    def __init__(self, ai_game):
        """Ініціалізує зірку """
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_width = self.settings.screen_width
        self.screen_height = self.settings.screen_height
        self.reset()
    
    def reset(self):
        """Встановлює початкові значенння параметрів зірки."""
        self.x = random.randint(0, self.settings.screen_width) - self.screen_width // 2
        self.y = random.randint(0, self.settings.screen_height) - self.screen_height // 2
        self.z = 256
        self.color = self.settings.star_start_color
    
    def update(self):
        """Оновлює зіркy."""
        #Змінюємо z координату зірки
        self.z -= self.settings.star_speed
        #Обчислюємо поточні координати зірки
        x = self.x *256/ self.z
        y = self.y *256/ self.z
        # Якщо зірка вийшла за межі екрану
        if (
            self.z <= 0 
            or x < -self.settings.screen_width // 2 
            or x > self.settings.screen_width // 2 
            or y < -self.settings.screen_height // 2 
            or y > self.settings.screen_height // 2 
            
        ):
            self.reset()
        
        # Збільшуємо яскравість зірки
        if self.color < self.settings.star_color_limit:
            self.color += self.settings.star_color_step
            if self.color > self.settings.star_color_limit:
                self.color = self.settings.star_color_limit - 1
        
        # Відображаємо зірку на екрані
        x = round(self.x * 256 / self.z) + self.settings.screen_width // 2
        y = round(self.y * 256 / self.z) + self.settings.screen_height // 2
        pg.draw.circle(
            self.screen,
            (self.color, self.color, self.color),
            (x, y),
            self.settings.star_radius
        )