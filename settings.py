class Settings:
    """Клас для зберігання всіх налаштувань гри"""
    
    def __init__(self):
        """Ініціалізує налаштування гри."""
        #Параметри екрану
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = "grey90"
        
        # Налаштування корабля
        self.ship_speed = 1.5

        # Налаштування снаряда
        self.bullet_speed = 2
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = "firebrick2"
        self.bullets_allowed = 3