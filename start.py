import sys

import pygame as pg

from settings import Settings
from ship import Ship


class AlienInvasion:
    """Клас для керування ресурсами та основною логікою гри."""

    def __init__(self):
        """Ініціалізує гру та створює її ресурси."""
        pg.init()
        self.clock = pg.time.Clock()
        self.settings = Settings()

        self.screen = pg.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
            )
        pg.display.set_caption("Alien Invasion")

        # Смворення ігрових об'єктів
        self.ship = Ship(self)

    def run_game(self):
        """Запускає основний цикл гри."""
        while True:
            self._check_events()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """Відстежує події клавіатури та миші."""
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
    
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

        