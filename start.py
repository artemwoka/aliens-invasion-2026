import sys
from time import sleep

import pygame as pg

from alien import Alien
from bullet import Bullet
from button import Button
from game_stats import GameStats
from scoreboard import Scoreboard
from settings import Settings
from ship import Ship


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
        
        # Створює екземпляр для зберігання ігрової статистики.
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        # Смворення ігрових об'єктів
        self.ship = Ship(self)
        self.bullets = pg.sprite.Group()
        self.aliens = pg.sprite.Group()

        self._create_fleet()

        # Створює кнопку Play.
        self.play_button = Button(self, "Play")

        # Гра запущена в неактивному стані.
        self.stats.game_active = False

    def run_game(self):
        """Запускає основний цикл гри."""
        while True:
            self._check_events()
            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
            self._update_screen()
            self.clock.tick(60)
    
    def _change_fleet_direction(self):
        """Опускає весь флот і змінює його напрямок."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1
    
    def _check_alliens_bottom(self):
        """Перевіряє, чи досягнув який-небудь прибулець нижнього краю екрану."""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # Зіткнення відбувається так само, як і при зіткненні з кораблем.
                self._ship_hit()
                break


    def _check_events(self):
        """Відстежує події клавіатури та миші."""
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            elif event.type == pg.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pg.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pg.MOUSEBUTTONDOWN:
                mouse_pos = pg.mouse.get_pos()
                self._check_play_button(mouse_pos)
            
            
    
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
                elif event.key == pg.K_SPACE:
                    self.fire_bullet()

    def _check_fleet_edges(self):
        """Реагує на досягнення прибульцем краю екрану."""
        for alien in self.aliens.sprites():
            if alien._check_edges():
                self._change_fleet_direction()
                break

    def _check_keyup_events(self, event):
        """Відстежує відпускання клавіш."""
        if event.type == pg.KEYUP:
                if event.key == pg.K_RIGHT:
                    # Зупинка руху корабля вправо
                    self.ship.moving_right = False
                elif event.key == pg.K_LEFT:
                    # Зупинка руху корабля вліво
                    self.ship.moving_left = False
        
    def _check_play_button(self, mouse_pos):
        """Починає нову гру при натисканні кнопки Play."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            # Скидає налаштування гри до початкових значень.
            self.settings.initialize_dynamic_settings()
            self.stats.game_active = True
            self.stats.reset_stats()

            self.aliens.empty()
            self.bullets.empty()
            self._create_fleet()
            self.ship.center_ship()

            # Сховати курсор миші.
            pg.mouse.set_visible(False)

    def _create_alien(self, x_position, y_position):
        new_alien = Alien(self)
        self.aliens.add(new_alien)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
    
    def _create_fleet(self):
        """Створює флот прибульців."""
        #Строрення прибульця і визначення кількості прибульців, які помістяться в ряд.
        alien = Alien(self)
        self.aliens.add(alien)
        alien_width, alien_height = alien.rect.size

        current_x, current_y = alien_width, alien_height
        while current_y < (self.settings.screen_height - 3 * alien_height):
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += alien_width * 2

            # Кінець ряду
            current_x = alien_width
            current_y += alien_height * 2
           

    def fire_bullet(self):
        """Створює новий снаряд та додає його до групи снарядів."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _ship_hit(self):
        """Обробляє зіткнення корабля з прибульцем."""
        if self.stats.ships_left > 0:
             
            self.stats.ships_left -= 1
            self.aliens.empty()
            self.bullets.empty()
            self._create_fleet()
            self.ship.center_ship()
            # Пауза
            sleep(0.5)
        else:
            self.stats.game_active = False
            pg.mouse.set_visible(True)
            
    
    def _update_aliens(self):
        """Оновлює позиції всіх прибульців у флоті."""
        self._check_fleet_edges()
        self.aliens.update()
        # Перевірка зіткнення прибульців з кораблем
        if pg.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        self._check_alliens_bottom()
           

    def _update_bullets(self):
        """Оновлює позиції снарядів та видаляє старі снаряди."""
        self.bullets.update()
        # Перевірка потраплянь в прибульців
        collisions = pg.sprite.groupcollide(self.bullets, self.aliens,
                                                 True, True)
        if not self.aliens:
            # Знищує існуючі снаряди та створює новий флот.
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()
        
    def _update_screen(self):
        """Оновлює зображення на екрані та переходить до нового екрану."""
        #Оновлює екран під час кожного проходу циклу.
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        self.ship.blitme()

        # Виводить інформацію про рахунок.
        self.sb.show_score()

        #Кнопка Play відображається лише тоді, коли гра неактивна.
        if not self.stats.game_active:
            self.play_button.draw_button()

        #Відображає останній екран.
        pg.display.flip()


if __name__ == '__main__':
    #Створює екземпляр гри та запускає її.
    ai = AlienInvasion()
    ai.run_game()

        