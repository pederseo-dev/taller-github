#!/usr/bin/env python3
"""
principal.py - Módulo principal del juego Wordle
"""

import sys

from datos_palabras import seleccionar_palabra_secreta
from validacion import verificar_victoria
from evaluacion import evaluar_intento
from pantalla import (
    mostrar_mensaje_bienvenida,
    mostrar_retroalimentacion,
    mostrar_mensaje_victoria,
    mostrar_mensaje_derrota
)
from manejo_entrada import obtener_intento_jugador


def jugar():
    """Función principal que ejecuta el juego completo."""
    LONGITUD_PALABRA = 5
    INTENTOS_MAXIMOS = 6
    
    # Iniciar juego
    palabra_secreta = seleccionar_palabra_secreta()
    mostrar_mensaje_bienvenida(LONGITUD_PALABRA, INTENTOS_MAXIMOS)
    
    # Bucle principal
    for intento in range(1, INTENTOS_MAXIMOS + 1):
        # Obtener intento del jugador
        palabra_intento = obtener_intento_jugador(intento, INTENTOS_MAXIMOS)
        
        # Evaluar intento
        estados = evaluar_intento(palabra_secreta, palabra_intento)
        
        # Mostrar retroalimentación
        mostrar_retroalimentacion(palabra_intento, estados)
        
        # Verificar victoria
        if verificar_victoria(estados):
            mostrar_mensaje_victoria(palabra_secreta, intento)
            return
    
    # Si se acabaron los intentos
    mostrar_mensaje_derrota(palabra_secreta)


def principal():
    """Punto de entrada del programa."""
    try:
        jugar()
    except KeyboardInterrupt:
        print('\n\nJuego interrumpido. ¡Hasta luego!')
        sys.exit(0)


if __name__ == '__main__':
    principal()
