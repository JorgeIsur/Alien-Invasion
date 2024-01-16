import sys

import pygame


def check_events(ship):
    """Responde a entradas de teclado y eventos del mouse"""
    # esperar eventos de teclado y mouse
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def check_keydown_events(event, ship):
    """Manejar el presionado de teclas"""
    if event.key == pygame.K_RIGHT:
        # mover la nave a la derecha
        ship.moving_right = True
    if event.key == pygame.K_LEFT:
        # mover la nave a la izquierda
        ship.moving_left = True


def check_keyup_events(event, ship):
    """Manejar el liberado de teclas"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False


def update_screen(ai_settings, screen, ship):
    """Actualiza imagenes en la pantalla"""
    # redibujar la pantalla en cada iteracion del ciclo
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    # mostrar la pantalla
    pygame.display.flip()
