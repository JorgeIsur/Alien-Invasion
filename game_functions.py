import sys

import pygame

from bullet import Bullet
from alien import Alien


def check_events(ai_settings, screen, ship, bullets):
    """Responde a entradas de teclado y eventos del mouse"""
    # esperar eventos de teclado y mouse
    for event in pygame.event.get():
        # print(event.type)
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
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, ship):
    """Manejar el liberado de teclas"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False


def update_screen(ai_settings, screen, ship, aliens, bullets):
    """Actualiza imagenes en la pantalla"""
    # redibujar la pantalla en cada iteracion del ciclo
    screen.fill(ai_settings.bg_color)
    # REDIBUJAR TODAS LAS BALAS DETRAS DE LA NAVE Y ALIENS
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)

    # mostrar la pantalla
    pygame.display.flip()


def update_bullets(bullets):
    """Actualizar la posición de las balas y eliminar balas innecesarias"""
    # Actualizar posición de balas
    bullets.update()
    # Eliminar las balas que han desaparecido de la pantalla
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    # verificar que las balas se eliminaron
    # print(len(bullets))


def fire_bullet(ai_settings, screen, ship, bullets):
    """Disparar una bala si el limite de balas no se ha sobrepasado"""
    if len(bullets) < ai_settings.bullets_allowed:
        # Crear una nueva bala y añadirla al grupo de balas
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def create_fleet(ai_settings, screen, aliens):
    """Crear una flota llena de aliens"""
    # Crear un alien y determinar el numero de aliens por fila
    # Espacio entre aliens es igual al ancho de un alien
    alien = Alien(ai_settings,screen)
    alien_width = alien.rect.width
    available_space_x = ai_settings.screen_width - 2*alien_width
    number_aliens_x = int(available_space_x/(2*alien_width))

    # Crear la primera fila de aliens
    for alien_number in range(number_aliens_x):
        # Crear un alien y ponerlo en la fila
        alien = Alien(ai_settings,screen)
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        aliens.add(alien)