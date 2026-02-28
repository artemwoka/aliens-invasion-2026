class Settings:
    """Клас для зберігання всіх налаштувань гри"""
    
    def __init__(self):
        """Ініціалізує налаштування гри."""
        #Параметри екрану
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = "grey90"
        
        # Налаштування корабля
        self.ship_limit = 3

        # Налаштування снаряда
        self.bullet_width = 800
        self.bullet_height = 15
        self.bullet_color = "firebrick2"
        self.bullets_allowed = 3

        # Налаштування прибульців
        
        self.fleet_drop_speed = 10
        

        # Темп прискорення гри
        self.speedup_scale = 1.2
        self.score_scale = 1.5

        self.initialize_dynamic_settings()
    
    def initialize_dynamic_settings(self):
        """Ініціалізує налаштування, які змінюються впродовж гри."""

        self.ship_speed = 1.5
        self.bullet_speed = 5.0
        self.alien_speed = 1.0

        # fleet_direction = 1 означає рух праворуч, а -1 - рух ліворуч.
        self.fleet_direction = 1

        # Підрахунок очок
        self.alien_points = 50

    def increase_speed(self):
        """Збільшує налаштування швидкості."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)

