#!/usr/bin/env python3
"""
pantalla.py - Módulo para manejo de la interfaz de usuario y visualización
"""


def mostrar_mensaje_bienvenida(longitud_palabra=5, intentos_maximos=6):
    """Muestra el mensaje de bienvenida del juego."""
    print("=" * 50)
    print("      WORDLE TERMINAL - Taller de Git")
    print("=" * 50)
    print(f"\nAdivina la palabra de {longitud_palabra} letras.")
    print(f"Tienes {intentos_maximos} intentos.\n")
    print("Símbolos:")
    print("  ✓ = Letra correcta en posición correcta")
    print("  ? = Letra presente pero en otra posición")
    print("  X = Letra no presente en la palabra")
    print("=" * 50)
    print()


def mostrar_retroalimentacion(intento, estados):
    """Muestra el feedback visual del intento."""
    simbolos = {
        'correcta': '✓',
        'presente': '?',
        'ausente': 'X'
    }
    
    # Línea con las letras
    letras = ' '.join(letra.upper() for letra in intento)
    print(f"  {letras}")
    
    # Línea con los símbolos
    retroalimentacion = ' '.join(simbolos[estado] for estado in estados)
    print(f"  {retroalimentacion}")
    print()


def mostrar_mensaje_victoria(secreta, intentos):
    """Muestra mensaje de victoria."""
    print("=" * 50)
    print(f"¡FELICIDADES! 🎉")
    print(f"Adivinaste la palabra '{secreta.upper()}' en {intentos} intento(s).")
    print("=" * 50)


def mostrar_mensaje_derrota(secreta):
    """Muestra mensaje de derrota."""
    print("=" * 50)
    print(f"¡Juego Terminado!")
    print(f"La palabra era: {secreta.upper()}")
    print("¡Suerte la próxima!")
    print("=" * 50)
