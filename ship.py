import pygame

class Ship():

    def __init__(self,ai_settings,screen):
        """Inicializa la nave y determina su posición inicial"""
        self.screen = screen
        self.ai_settings = ai_settings

        # Carga la imagen de la nave
        self.image = pygame.image.load('images/kanye.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # posiciona cada nueva nave al fondo, en el centro de la pantalla
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Guardar un valor decimal para el centramiento de la nave
        self.center = float(self.rect.centerx)

        # bandera de movimiento
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Actualiza la posición de la nave en base al valor de la bandera de movimiento"""
        # actualizar el valor del centro de la nave, no el rectangulo
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        elif self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        self.rect.centerx = self.center

    def blitme(self):
        """Dibuja la nave en la posicion actual"""
        self.screen.blit(self.image,self.rect)