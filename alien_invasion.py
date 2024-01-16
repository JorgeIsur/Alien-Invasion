import pygame

# importar configuraciones
from settings import Settings

# importar objeto de la nave
from ship import Ship

# importar funciones del juego
import game_functions as gf


def run_game():
    # inicializar el juego, configuraciones y crear un objeto de pantalla
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # instanciar la nave
    ship = Ship(ai_settings,screen)

    # inicializar el ciclo principal para el juego
    while True:
        # manejador de eventos
        gf.check_events(ship)
        # Actualizar posición de la nave
        ship.update()
        # actualizador de pantalla
        gf.update_screen(ai_settings,screen,ship)


run_game()
