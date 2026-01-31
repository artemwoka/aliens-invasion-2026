import sys

import pygame as pg

from settings import Settings
from ship import Ship
from bullet import Bullet


class AlienInvasion:
    """Клас для керування ресурсами та основною логікою гри."""

    def __init__(self):
        """Ініціалізує гру та створює її ресурси."""
        pg.init()
        self.clock = pg.time.Clock()
        self.settings = Settings()

        self.screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pg.display.set_caption("Alien Invasion")

        # Смворення ігрових об'єктів
        self.ship = Ship(self)
        self.bullets = pg.sprite.Group()

    def run_game(self):
        """Запускає основний цикл гри."""
        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """Відстежує події клавіатури та миші."""
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            elif event.type == pg.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pg.KEYUP:
                self._check_keyup_events(event)
            
            
    
    def _check_keydown_events(self, event):
        """Відстежує натискання клавіш."""
        if event.type == pg.KEYDOWN:
                if event.key == pg.K_RIGHT:
                    # Рух корабля вправо
                    self.ship.moving_right = True
                elif event.key == pg.K_LEFT:
                    # Рух корабля вліво
                    self.ship.moving_left = True
                elif event.key == pg.K_ESCAPE:
                    sys.exit()
    
    def _check_keyup_events(self, event):
        """Відстежує відпускання клавіш."""
        if event.type == pg.KEYUP:
                if event.key == pg.K_RIGHT:
                    # Зупинка руху корабля вправо
                    self.ship.moving_right = False
                elif event.key == pg.K_LEFT:
                    # Зупинка руху корабля вліво
                    self.ship.moving_left = False

            
    
    def _update_screen(self):
        """Оновлює зображення на екрані та переходить до нового екрану."""
        #Оновлює екран під час кожного проходу циклу.
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        #Відображає останній екран.
        pg.display.flip()


if __name__ == '__main__':
    #Створює екземпляр гри та запускає її.
    ai = AlienInvasion()
    ai.run_game()

        