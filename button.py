import pygame as pg



class Button:
    """Клас для керування кнопками в грі."""
    
    def __init__(self, ai_game, msg):
        """Ініціалізує атрибути кнопки."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        
        # Призначення розмірів та властивостей кнопки.
        self.width, self.height = 200, 50
        self.button_color = "green"
        self.text_color = "white"
        self.font = pg.font.SysFont(None, 48)

        # Створення об'єкта rect кнопки та вирівнювання по центру екрану.
        self.rect = pg.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # Текст кнопки повинен бути підготовлений лише один раз.
        self._prep_msg(msg)

    def draw_button(self):
        """Відображає пусту кнопку та потім повідомлення."""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

    def _prep_msg(self, msg):
        """Перетворює msg в прямокутник та вирівнює текст по центру кнопки."""
        self.msg_image = self.font.render(msg, True, self.text_color,self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center