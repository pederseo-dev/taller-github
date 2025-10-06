#!/usr/bin/env python3
"""
manejo_entrada.py - Módulo para manejo de entrada del usuario
"""

from validacion import validar_intento


def obtener_intento_jugador(numero_intento, intentos_maximos):
    """
    Solicita y retorna el intento del jugador.
    Valida que sea correcto antes de retornarlo.
    """
    while True:
        prompt = f"Intento {numero_intento}/{intentos_maximos} - Tu palabra: "
        intento = input(prompt).strip().lower()
        
        es_valido, mensaje_error = validar_intento(intento)
        
        if es_valido:
            return intento
        else:
            print(f"  Error: {mensaje_error} Intenta de nuevo.\n")
