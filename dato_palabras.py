import random

def obtener_lista_palabras():
    lista = [
    "barro", "juego", "zumba", "calor", "hielo", "lanza", "borde", "salsa", "pulso",
    "brisa", "tacho", "fluir", "nubes", "vigor", "joven", "raton",
    "marea", "llama", "tenaz", "crisp"
]
    lista_minus=[palabra.lower() for palabra in lista]
    return lista_minus

def seleccionar_palabra_secreta():
    palabra= obtener_lista_palabras()
    return random.choice(palabra)

