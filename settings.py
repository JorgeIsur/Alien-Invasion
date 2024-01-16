class Settings():
    """Una clase para almacenar las configuraciones de 'ALIEN INVASION' """
    def __init__(self):
        """Inicializar las configuraciones del juego"""
        # Configuracion de pantalla
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)
        # Configuraciones de la nave
        self.ship_speed_factor = 1.5
