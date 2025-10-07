
def contar_letras_disponibles(secreta, intento):
    secreta_lower = secreta.lower()
    intento_lower = intento.lower()
    conteo_disponibles = {}
    
    for i in range(len(secreta_lower)):
        if secreta_lower[i] != intento_lower[i]:
            letra_secreta = secreta_lower[i]
            conteo_disponibles[letra_secreta] = conteo_disponibles.get(letra_secreta, 0) + 1
    return conteo_disponibles

def evaluar_intento(secreta, intento):
    secreta = secreta.lower()
    intento = intento.lower()

    # Verificar longitud
    if len(secreta) != len(intento):
        raise ValueError("Las palabras deben tener la misma longitud.")

    # 2. Crear lista de estados inicializada con None
    estados = [None] * len(secreta)

    # 3. Obtener conteo de letras disponibles
    disponibles = contar_letras_disponibles(secreta, intento)

    # 4. PRIMER PASO: Marcar las 'correcta'
    for i in range(len(secreta)):
        if intento[i] == secreta[i]:
            estados[i] = 'correcta'

    # 5. SEGUNDO PASO: Marcar 'presente' o 'ausente'
    for i in range(len(secreta)):
        if estados[i] is None:  # aún no evaluada
            letra = intento[i]
            if letra in disponibles and disponibles[letra] > 0:
                estados[i] = 'presente'
                disponibles[letra] -= 1
            else:
                estados[i] = 'ausente'

    # 6. Retornar lista de estados
    return estados



