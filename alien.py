import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Una clase para representar un solo alien en la flota"""

    def __init__(self,ai_settings, screen):
        """Inicializar un alien y su posición inicial"""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Cargar la imagen de un alien y su atributo rectangular
        self.image = pygame.image.load('images/taylor.bmp')
        self.rect = self.image.get_rect()

        # Inicializar cada nuevo alien cerca de la esquina superior izquierda de la pantalla
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Almacenar la posición exacta de cada alien
        self.x = float(self.rect.x)

    def blitme(self):
        """Dibujar el alien en su posición actual"""
        self.screen.blit(self.image,self.rect)
