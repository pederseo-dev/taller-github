#!/usr/bin/env python3
"""
datos_palabras.py - Módulo para manejo de palabras del juego Wordle
"""

import random


def obtener_lista_palabras():
    """Retorna la lista de palabras posibles del juego."""
    return [
        "amigo", "perro", "cielo", "libro", "salud",
        "gente", "grano", "noche", "verde", "blusa",
        "plaza", "avion", "coral", "sabor", "fuego",
        "llave", "mesa", "silla", "puerta", "rueda",
        "brisa", "sonar", "punto", "marco", "arena",
        "hojas", "dulce", "firme", "claro", "roble",
        "campo", "huevo"
    ]


def seleccionar_palabra_secreta():
    """Selecciona una palabra aleatoria de la lista."""
    palabras = obtener_lista_palabras()
    return random.choice(palabras)
