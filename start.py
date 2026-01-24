import sys

import pygame as pg


class AlienInvasion:
    """Клас для керування ресурсами та основною логікою гри."""

    def __init__(self):
        """Ініціалізує гру та створює її ресурси."""
        pg.init()
        self.clock = pg.time.Clock()

        self.screen = pg.display.set_mode((1200, 700))
        pg.display.set_caption("Alien Invasion")

        #Призначає колір фону.
        self.bg_color = (230, 230, 230)

    def run_game(self):
        """Запускає основний цикл гри."""
        while True:
            #Відстежує події клавіатури та миші.
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit()
            
            #Заповнює екран кольором фону.
            self.screen.fill(self.bg_color)

            #Відображає останній екран.
            pg.display.flip()
            self.clock.tick(60)


if __name__ == '__main__':
    #Створює екземпляр гри та запускає її.
    ai = AlienInvasion()
    ai.run_game()

        