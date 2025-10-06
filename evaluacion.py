#!/usr/bin/env python3
"""
evaluacion.py - Módulo para evaluación de intentos y conteo de letras
"""


def contar_letras_disponibles(secreta, intento):
    """
    Cuenta las letras disponibles en la palabra secreta
    (excluyendo las que ya están en posición correcta).
    Retorna un diccionario con los conteos.
    """
    secreta = secreta.lower()
    intento = intento.lower()
    longitud_palabra = len(secreta)
    
    conteo_letras = {}
    
    for i in range(longitud_palabra):
        if secreta[i] != intento[i]:
            letra = secreta[i]
            conteo_letras[letra] = conteo_letras.get(letra, 0) + 1
    
    return conteo_letras


def evaluar_intento(secreta, intento):
    """
    Evalúa el intento comparándolo con la palabra secreta.
    Retorna una lista de estados: 'correcta', 'presente', 'ausente'
    """
    secreta = secreta.lower()
    intento = intento.lower()
    longitud_palabra = len(secreta)
    
    estados = [None] * longitud_palabra
    
    # Obtener conteo de letras disponibles
    conteo_letras = contar_letras_disponibles(secreta, intento)
    
    # Paso 1: Marcar posiciones correctas
    for i in range(longitud_palabra):
        if intento[i] == secreta[i]:
            estados[i] = 'correcta'
    
    # Paso 2: Marcar letras presentes o ausentes
    for i in range(longitud_palabra):
        if estados[i] is not None:
            continue
        
        letra = intento[i]
        if conteo_letras.get(letra, 0) > 0:
            estados[i] = 'presente'
            conteo_letras[letra] -= 1
        else:
            estados[i] = 'ausente'
    
    return estados
