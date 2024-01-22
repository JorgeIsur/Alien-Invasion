import pygame

# importar configuraciones
from settings import Settings

# importar objeto de la nave
from ship import Ship

# importar funciones del juego
import game_functions as gf

# importar agrupamiento
from pygame.sprite import Group


def run_game():
    # inicializar el juego, configuraciones y crear un objeto de pantalla
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Taylor's Invasion")

    # instanciar la nave
    ship = Ship(ai_settings,screen)
    # crear un grupo para almacenar balas en el
    bullets = Group()
    # crear un grupo de aliens
    aliens = Group()
    # crear una flota de aliens
    gf.create_fleet(ai_settings,screen,aliens)

    # inicializar el ciclo principal para el juego
    while True:
        # manejador de eventos
        gf.check_events(ai_settings, screen, ship, bullets)
        # Actualizar posición de la nave
        ship.update()
        # Actualizar posición de balas
        gf.update_bullets(bullets)
        # actualizador de pantalla
        gf.update_screen(ai_settings,screen,ship, aliens, bullets)


run_game()
