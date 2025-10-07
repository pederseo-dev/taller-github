secreta = "perro"
intento = "puede"

def contar_letras_disponibles(secreta, intento):
    secreta_lower = secreta.lower()
    intento_lower = intento.lower()
    conteo_disponibles = {}
    
    for i in range(len(secreta_lower)):
        if secreta_lower[i] != intento_lower[i]:
            letra_secreta = secreta_lower[i]
            conteo_disponibles[letra_secreta] = conteo_disponibles.get(letra_secreta, 0) + 1
    return conteo_disponibles
contar = contar_letras_disponibles(secreta, intento)
print(contar)