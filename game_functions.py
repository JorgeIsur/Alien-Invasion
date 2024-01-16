import sys

import pygame

from bullet import Bullet


def check_events(ai_settings, screen, ship, bullets):
    """Responde a entradas de teclado y eventos del mouse"""
    # esperar eventos de teclado y mouse
    for event in pygame.event.get():
        #print(event.type)
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """Manejar el presionado de teclas"""
    if event.key == pygame.K_RIGHT:
        # mover la nave a la derecha
        ship.moving_right = True
    if event.key == pygame.K_LEFT:
        # mover la nave a la izquierda
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        #print("Espacio")
        # Crear una nueva bala y añadirla al grupo de balas
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def check_keyup_events(event, ship):
    """Manejar el liberado de teclas"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False


def update_screen(ai_settings, screen, ship, bullets):
    """Actualiza imagenes en la pantalla"""
    # redibujar la pantalla en cada iteracion del ciclo
    screen.fill(ai_settings.bg_color)
    # REDIBUJAR TODAS LAS BALAS DETRAS DE LA NAVE Y ALIENS
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()

    # mostrar la pantalla
    pygame.display.flip()
