#!/usr/bin/env python3
"""
validacion.py - Módulo para validación de intentos y verificación de victoria
"""


def validar_intento(intento, longitud_palabra=5):
    """
    Valida que el intento sea correcto.
    Retorna (es_valido, mensaje_error)
    """
    if len(intento) != longitud_palabra:
        return False, f"Debe tener exactamente {longitud_palabra} letras."
    
    if not intento.isalpha():
        return False, "Solo se permiten letras."
    
    return True, ""


def verificar_victoria(estados):
    """Verifica si el jugador ganó (todas las letras correctas)."""
    return all(estado == 'correcta' for estado in estados)
