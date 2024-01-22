class Settings():
    """Una clase para almacenar las configuraciones de 'ALIEN INVASION' """

    def __init__(self):
        """Inicializar las configuraciones del juego"""
        # Configuracion de pantalla
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (194, 26, 52)
        # Configuraciones de la nave
        self.ship_speed_factor = 1.5
        # Configuracinoes de las balas
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3
