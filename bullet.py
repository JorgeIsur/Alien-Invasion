import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Clase que define las balas disparadas desde la nave"""

    def __init__(self, ai_settings, screen, ship):
        """Crear un objeto 'Bala' en la posición actual de la nave"""
        super(Bullet,self).__init__()
        self.screen = screen

        # Crear un rectangulo para la bala en (0, 0) y después ajustar a la posición correcta
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # Almacenar la posición como un valor decimal
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """Mover la bala en la pantalla (hacia arriba)"""
        # Actualizar la posición decimal de la bala
        self.y -= self.speed_factor
        # Actualizar la posición del rectangulo
        self.rect.y = self.y

    def draw_bullet(self):
        """Dibujar la bala en la pantalla"""
        pygame.draw.rect(self.screen, self.color, self.rect)
