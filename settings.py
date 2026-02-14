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
        self.ship_limit = 3

        # Налаштування снаряда
        self.bullet_speed = 5.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = "firebrick2"
        self.bullets_allowed = 3

        # Налаштування прибульців
        self.alien_speed = 1
        self.fleet_drop_speed = 100
        # fleet_direction = 1 означає рух праворуч, а -1 - рух ліворуч.
        self.fleet_direction = 1